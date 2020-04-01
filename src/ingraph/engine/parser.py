# Copyright 2020 Farzad Senart and Lionel Suss. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import ast
import importlib.resources
import inspect
from functools import reduce
from types import FunctionType, ModuleType
from typing import (Any, Dict, List, NamedTuple, NoReturn, Optional, Sequence,
                    Tuple, Type, Union)

import parso

from . import core

TRANSFORMERS: List[Type["Transformer"]]


def process(source: str, filename: str, module: ModuleType) -> None:
    tree = parse(source, filename)
    code = compile(tree, filename, "exec")
    builtins = getattr(module, "__builtins__", {})
    builtins.update(
        __build_class__=__build_class__,  # type: ignore
        str=str,
        int=int,
        float=float,
        **{_n(t): t for t in [NameError]},
        **{
            _n(t): t
            for t in [
                core.Boolean,
                core.Number,
                core.String,
                core.Map,
                core.new_list,
                core.CustomResource,
                core.ExternalResource,
            ]
        },
        **{
            _n(v): v
            for t in TRANSFORMERS
            for (k, v) in inspect.getmembers(t, predicate=inspect.isfunction)
            if k.startswith("proxy_")
        },
    )
    setattr(module, "__builtins__", builtins)
    exec(code, vars(module))


def parse(source: str, filename: str) -> ast.Module:
    with importlib.resources.path(__package__, "Grammar") as path:
        grammar = parso.load_grammar(path=path)
    module = grammar.parse(source)
    errs = grammar.iter_errors(module)
    if errs:
        msg = errs[0].message.replace("SyntaxError: ", "")
        raise SyntaxError(msg, (filename, *errs[0].start_pos, None))
    return reduce(
        lambda tree, trans: ast.fix_missing_locations(
            trans(source, filename).visit(_setparents(tree))
        ),
        TRANSFORMERS,
        ast.parse(source, filename),
    )


def _setparent(node: ast.AST, parent: Optional[ast.AST]) -> ast.AST:
    setattr(node, "_ig_parent", parent)
    return node


def _getparent(node: ast.AST) -> Optional[ast.AST]:
    return getattr(node, "_ig_parent", None)


def _setparents(node: ast.AST) -> ast.AST:
    for parent in ast.walk(node):
        for child in ast.iter_child_nodes(parent):
            _setparent(child, parent)
    return node


def _n(fn: Any) -> str:
    return f"_ig_{fn.__qualname__.replace('.', '_')}"


class Location(NamedTuple):
    filename: ast.Constant
    lines: ast.Tuple
    columns: ast.Tuple
    source: ast.Constant


class Transformer(ast.NodeTransformer):
    def __init__(self, source: str, filename: str):
        self._source = source
        self._filename = filename

    def location(self, node: ast.AST) -> Location:
        filename = ast.Constant(value=self._filename)
        lstart = ast.Constant(value=getattr(node, "lineno", 0))
        lend = ast.Constant(value=getattr(node, "end_lineno", 0))
        lines = ast.Tuple(elts=[lstart, lend], ctx=ast.Load())
        cstart = ast.Constant(value=getattr(node, "col_offset", 0))
        cend = ast.Constant(value=getattr(node, "end_col_offset", 0))
        columns = ast.Tuple(elts=[cstart, cend], ctx=ast.Load())
        source = ast.Constant(value=ast.get_source_segment(self._source, node))
        return Location(filename, lines, columns, source)

    def error(
        self, node: ast.AST, msg: str = "invalid syntax"
    ) -> SyntaxError:  # pragma: no cover
        parent = _getparent(node)
        line = getattr(node, "lineno", getattr(parent, "lineno", 1))
        col = getattr(node, "col_offset", getattr(parent, "col_offset", 0))
        src = ast.get_source_segment(self._source, node)
        if not src and parent is not None:
            src = ast.get_source_segment(self._source, parent)
        return SyntaxError(msg, (self._filename, line, col, src))


class PrivateChecker(Transformer):

    message = "names cannot start with an underscore"

    def visit_Attribute(self, node: ast.Attribute) -> ast.Attribute:
        self.generic_visit(node)
        if node.attr.startswith("_"):
            raise self.error(node, self.message)
        return node

    def visit_Call(self, node: ast.Call) -> ast.Call:
        self.generic_visit(node)
        for arg in node.keywords:
            if arg.arg and arg.arg.startswith("_"):
                raise self.error(arg, self.message)
        return node

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
        self.generic_visit(node)
        if node.name.startswith("_"):
            raise self.error(node, self.message)
        return node

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        self.generic_visit(node)
        for arg in node.args.args:
            if arg.arg.startswith("_"):
                raise self.error(arg, self.message)
        return node

    def visit_ImportFrom(self, node: ast.ImportFrom) -> ast.ImportFrom:
        self.generic_visit(node)
        for name in node.names:
            aliases = [name.name, name.asname if name.asname is not None else ""]
            if any(a.startswith("_") for a in aliases):
                raise self.error(node, self.message)
        return node

    def visit_Name(self, node: ast.Name) -> ast.Name:
        self.generic_visit(node)
        if node.id.startswith("_"):
            raise self.error(node, self.message)
        return node


class SignatureModifier(Transformer):
    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        self.generic_visit(node)
        node.args.kwonlyargs = node.args.args[1:]
        node.args.args = node.args.args[0:1]
        count = len(node.args.kwonlyargs) - len(node.args.defaults)
        node.args.kw_defaults = count * [None] + node.args.defaults  # type: ignore
        node.args.defaults = []
        return node


class ImmutabilityGuard(Transformer):
    def visit_Assign(self, node: ast.Assign) -> Any:
        self.generic_visit(node)
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            return node
        expr = ast.Name(id=target.id, ctx=ast.Load())
        name = target.id
        check = ast.Try(
            body=[ast.Expr(expr)],
            handlers=[
                ast.ExceptHandler(
                    type=ast.Tuple(
                        elts=[ast.Name(id=_n(NameError), ctx=ast.Load())],
                        ctx=ast.Load(),
                    ),
                    name=None,
                    body=[ast.Expr(value=ast.Constant(value=Ellipsis))],
                )
            ],
            orelse=[
                ast.Raise(
                    exc=ast.Call(
                        func=ast.Name(
                            id=_n(ImmutabilityGuard.proxy_Assign), ctx=ast.Load()
                        ),
                        args=[ast.Constant(value=name)],
                        keywords=[],
                    ),
                    cause=None,
                )
            ],
            finalbody=[],
        )
        return [check, node]

    @staticmethod
    def proxy_Assign(target: str) -> NoReturn:
        raise TypeError(f"{target!r} is read-only")


class DefinitionWrapper(Transformer):
    def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
        self.generic_visit(node)
        if node.bases:
            node.bases = [
                ast.Name(id=_n(core.CustomResource), ctx=ast.Load()),
                *node.bases,
            ]
        else:
            node.bases = [ast.Name(id=_n(core.ExternalResource), ctx=ast.Load())]
        return node


class TypeWrapper(Transformer):
    def visit_Constant(self, node: ast.Constant) -> Union[ast.Constant, ast.Call]:
        self.generic_visit(node)
        parent = _getparent(node)
        value = node.value
        if value is Ellipsis or value is None:
            return node
        if isinstance(value, bool):
            proxy = _n(core.Boolean)
        elif isinstance(value, (int, float)):
            proxy = _n(core.Number)
        elif isinstance(value, str):
            proxy = _n(core.String)
        else:
            t = type(value)
            raise self.error(node, f"unsupported primitive type {t.__name__!r}")
        return ast.Call(
            func=ast.Name(id=proxy, ctx=ast.Load()), args=[node], keywords=[]
        )

    def visit_Dict(self, node: ast.Dict) -> ast.Call:
        self.generic_visit(node)
        return ast.Call(
            func=ast.Name(id=_n(core.Map), ctx=ast.Load()), args=[node], keywords=[],
        )

    def visit_List(self, node: ast.List) -> ast.Call:
        self.generic_visit(node)
        return ast.Call(
            func=ast.Name(id=_n(core.new_list), ctx=ast.Load()),
            args=[node],
            keywords=[],
        )

    def visit_UnaryOp(self, node: ast.UnaryOp) -> Any:
        if (
            isinstance(node.op, ast.USub)
            and isinstance(node.operand, ast.Constant)
            and isinstance(node.operand.value, (int, float))
        ):
            res = ast.Constant(value=ast.literal_eval(node))
            _setparent(res, _getparent(node))
            return self.visit_Constant(res)
        else:  # pragma: no cover
            self.generic_visit(node)
            return node


class LocationEnricher(Transformer):
    def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
        self.generic_visit(node)
        loc = self.location(node)
        node.body[0:0] = [
            ast.Assign(
                targets=[ast.Name(id=f"_ig_{attr}", ctx=ast.Store())],
                value=getattr(loc, attr),
            )
            for attr in ("filename", "lines", "columns", "source")
        ]
        return node


class CallWrapper(Transformer):
    def visit_Call(self, node: ast.Call) -> ast.Call:
        self.generic_visit(node)
        parent = _getparent(node)
        assert parent is not None
        if isinstance(parent, ast.Assign) and isinstance(parent.targets[0], ast.Name):
            name = ast.Constant(value=parent.targets[0].id)
        else:
            name = ast.Constant(value=None)
        definition = node.func
        filename, lines, columns, source = self.location(parent)
        return ast.Call(
            func=ast.Name(id=_n(CallWrapper.proxy_Call), ctx=ast.Load()),
            args=node.args,
            keywords=node.keywords
            + [
                ast.keyword(arg="_ig_name", value=name),
                ast.keyword(arg="_ig_definition", value=definition),
                ast.keyword(arg="_ig_filename", value=filename),
                ast.keyword(arg="_ig_lines", value=lines),
                ast.keyword(arg="_ig_columns", value=columns),
                ast.keyword(arg="_ig_source", value=source),
            ],
        )

    @staticmethod
    def proxy_Call(
        *args: Any,
        _ig_name: Optional[str],
        _ig_definition: Union[FunctionType, Type],
        _ig_filename: str,
        _ig_lines: Tuple[int, int],
        _ig_columns: Tuple[int, int],
        _ig_source: str,
        **kwargs: Any,
    ) -> Any:
        if _ig_definition in {int, float, str}:
            raise TypeError("invalid call")
        if not (
            isinstance(_ig_definition, type)
            and issubclass(
                _ig_definition,
                (
                    core.NativeResource,
                    core.CustomResource,
                    core.ExternalResource,
                    core.Asset,
                ),
            )
        ):
            return _ig_definition(*args, **kwargs)
        if _ig_name is None:
            raise TypeError("invalid resource instantiation")
        if issubclass(_ig_definition, core.Asset):
            return _ig_definition(*args, **kwargs)
        loc = core.Location(
            filename=_ig_filename,
            lines=_ig_lines,
            columns=_ig_columns,
            source=_ig_source,
        )
        with core.new_node(_ig_name, loc) as node:
            return _ig_definition(*args, _ig_node=node, **kwargs)  # type: ignore


class FStringWrapper(Transformer):
    def visit_FormattedValue(self, node: ast.FormattedValue) -> ast.Call:
        self.generic_visit(node)
        spec = node.format_spec
        return ast.Call(
            func=ast.Name(id=_n(self.proxy_FormattedValue), ctx=ast.Load()),
            args=[
                node.value,
                ast.Constant(value=node.conversion),
                spec if spec is not None else ast.Constant(value=""),
            ],
            keywords=[],
        )

    @staticmethod
    def proxy_FormattedValue(value: Any, conv: int, spec: Union[str, core.Sub]) -> Any:
        value = core.Formatter.ig_convert(value, chr(conv) if conv > -1 else None)
        value = core.Formatter.ig_format(value, spec)
        return value

    def visit_JoinedStr(self, node: ast.JoinedStr) -> ast.Call:
        self.generic_visit(node)
        return ast.Call(
            func=ast.Name(id=_n(self.proxy_JoinedStr), ctx=ast.Load()),
            args=[ast.List(elts=node.values, ctx=ast.Load())],
            keywords=[],
        )

    @staticmethod
    def proxy_JoinedStr(values: Sequence[Any]) -> core.Sub:
        fmts = ""
        kwargs: Dict[core.String, Any] = {}
        for v in values:
            fmt, kwarg = core.Formatter.ig_map(v, kwargs)
            fmts += fmt
            kwargs.update(kwarg)
        return core.Sub(core.String(fmts), core.Map(kwargs))


TRANSFORMERS = [
    PrivateChecker,
    SignatureModifier,
    ImmutabilityGuard,
    DefinitionWrapper,
    TypeWrapper,
    LocationEnricher,
    CallWrapper,
    FStringWrapper,
]
