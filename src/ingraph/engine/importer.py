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
import importlib
import importlib.abc
import importlib.util
import platform
import sys
import types
import typing
from contextlib import contextmanager
from functools import lru_cache
from importlib.machinery import ModuleSpec, PathFinder, SourceFileLoader
from importlib.util import spec_from_file_location
from pathlib import Path
from types import ModuleType
from typing import (Any, Dict, Final, Iterator, List, Mapping, Optional,
                    Sequence, Tuple, Type, Union, cast)

from mypy import api as mypyapi

from . import core, parser


def import_target(target: str) -> types.ModuleType:
    if Path(target).is_file():
        return import_file(Path(target))
    else:
        return import_module(target)


def import_file(path: Path) -> types.ModuleType:
    source = path.read_text("utf-8")
    filename = str(path)
    module = types.ModuleType("<adhoc>")
    import_content(source, filename, module)
    return module


def import_module(name: str) -> types.ModuleType:
    module = importlib.import_module(name)
    spec = module.__spec__
    if spec is None or not isinstance(
        spec.loader, (AWSPackageImporter, AWSModuleImporter, ExternalImporter)
    ):
        raise ModuleNotFoundError(f"No module named {name!r}")
    return module


def import_content(source: str, filename: str, module: ModuleType) -> None:
    _runmypy(filename)
    setattr(module, "__builtins__", dict(__import__=_hook__import__))
    parser.process(source, filename, module)


def _runmypy(filename: str) -> None:  # pragma: no cover
    null = "nul" if platform.system() == "Windows" else "/dev/null"
    hooks = sys.meta_path[:3]
    sys.meta_path[:] = sys.meta_path[3:]
    try:
        result = mypyapi.run(
            [
                "--python-version",
                "3.8",
                "--namespace-packages",
                "--disallow-untyped-calls",
                "--disallow-untyped-defs",
                "--disallow-incomplete-defs",
                "--no-implicit-reexport",
                "--strict",
                "--no-incremental",
                f"--cache-dir={null}",
                f"--config-file={null}",
                "--no-warn-unused-configs",
                "--pretty",
                # "--show-error-codes",
                filename,
            ]
        )
        if result[2] != 0:
            if result[0]:
                print(result[0], file=sys.stderr)
            sys.exit(result[2])
    finally:
        sys.meta_path[0:0] = hooks


class AWSPackageImporter(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(
        self,
        fullname: str,
        path: Optional[Sequence[Union[bytes, str]]],
        target: Optional[ModuleType] = None,
    ) -> Optional[ModuleSpec]:
        if fullname != "ingraph.aws":
            return None
        parent = Path(cast(Sequence[str], path)[0]) / "aws"
        origin = parent / "__init__.pyi"
        return spec_from_file_location(
            fullname, origin, loader=self, submodule_search_locations=[str(parent)]
        )

    @staticmethod
    def create_module(spec: ModuleSpec) -> Optional[ModuleType]:
        ...

    @staticmethod
    def exec_module(module: ModuleType) -> None:
        info = dict(__module__=module.__name__)
        for k, v in dict(
            ACCOUNT_ID=core.AccountID,
            AVAILABILITY_ZONES=core.AvailabilityZones,
            NOTIFICATION_ARNS=core.NotificationARNs,
            PARTITION=core.Partition,
            REGION=core.Region,
            STACK_ID=core.StackID,
            STACK_NAME=core.StackName,
            URL_SUFFIX=core.URLSuffix,
        ).items():
            setattr(module, k, v())
        for k, v in dict(
            b64encode=core.Base64Encoded, cidr=core.CIDR, Asset=core.Asset
        ).items():
            setattr(module, k, v)
        Tag = types.new_class(
            "Tag",
            (core.Property,),
            dict(module=module.__name__, params=[("Key", True), ("Value", True)]),
        )
        setattr(module, Tag.__name__, Tag)


class AWSModuleImporter(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(
        self,
        fullname: str,
        path: Optional[Sequence[Union[bytes, str]]],
        target: Optional[ModuleType] = None,
    ) -> Optional[ModuleSpec]:
        pre, _, post = fullname.rpartition(".")
        if pre != "ingraph.aws":
            return None
        origin = Path(cast(Sequence[str], path)[0]) / f"{post}.pyi"
        if not origin.is_file():
            raise ModuleNotFoundError(f"No module named {fullname!r}")
        return spec_from_file_location(fullname, origin, loader=self)

    @staticmethod
    def create_module(spec: ModuleSpec) -> Optional[ModuleType]:
        ...

    @staticmethod
    def exec_module(module: ModuleType) -> None:
        filename = module.__file__
        source = Path(filename).read_text()
        tree = ast.parse(source, filename, "exec")
        ns = _getawsns(tree)
        defs = _getawsdefs(module.__name__, source, ns, tree)
        for k, v in defs.items():
            setattr(module, k, v)


def _getawsns(tree: ast.Module) -> str:
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.Assign):
            return cast(ast.Constant, node.value).value
    raise NotImplementedError("namespace not found")  # pragma: no cover


def _getawsdefs(
    module: str, source: str, ns: str, tree: ast.Module
) -> Mapping[str, Type]:
    res = {}
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef):
            res[node.name] = _getawsdef(module, source, ns, node.name, node)
    return res


def _getawsdef(
    module: str, source: str, ns: str, name: str, tree: ast.ClassDef
) -> Type:
    kind = f"{ns}::{name}"
    attrs = _getawsattrs(source, tree)
    params = _getawsparams(tree)
    defn = types.new_class(
        name,
        (core.NativeResource,),
        dict(module=module, kind=kind, attrs=attrs, params=params),
    )
    defn.__doc__ = ast.get_docstring(tree)
    props = _getawsprops(module, tree)
    for k, v in props.items():
        setattr(defn, k, v)
    return defn


def _getawsprops(module: str, tree: ast.ClassDef) -> Mapping[str, Type]:
    res = {}
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef):
            res[node.name] = _getawsprop(module, node.name, node)
    return res


def _getawsprop(module: str, name: str, tree: ast.ClassDef) -> Type:
    params = _getawsparams(tree)
    return types.new_class(name, (core.Property,), dict(module=module, params=params),)


def _getawsattrs(source: str, tree: ast.ClassDef) -> Mapping[str, Type]:
    res = {}
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.AnnAssign):
            name = cast(ast.Name, node.target).id
            anno = node.annotation
            txt = cast(str, ast.get_source_segment(source, anno))
            res[name] = eval(txt)
    return res


def _getawsparams(tree: ast.ClassDef) -> Sequence[Tuple[str, bool]]:
    res = []
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.FunctionDef):
            args = node.args
            defs = args.kw_defaults
            for idx, arg in enumerate(args.kwonlyargs):
                res.append((arg.arg, defs[idx] is None))
    return res


@contextmanager
def aws_hook() -> Iterator[None]:
    hooks = [AWSPackageImporter(), AWSModuleImporter()]
    sys.meta_path[0:0] = hooks
    try:
        yield
    finally:
        sys.meta_path[:] = sys.meta_path[len(hooks) :]


class ExternalImporter(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(
        self,
        fullname: str,
        path: Optional[Sequence[Union[bytes, str]]],
        target: Optional[ModuleType] = None,
    ) -> Optional[ModuleSpec]:
        spec = PathFinder.find_spec(fullname, path, target)  # type: ignore
        if spec is None or not isinstance(spec.loader, SourceFileLoader):
            raise ModuleNotFoundError(f"No module named {fullname!r}")
        return spec_from_file_location(
            spec.name,
            cast(str, spec.origin),
            loader=self,
            submodule_search_locations=spec.submodule_search_locations,
        )

    @staticmethod
    def create_module(spec: ModuleSpec) -> Optional[ModuleType]:
        ...

    @staticmethod
    def exec_module(module: ModuleType) -> None:
        spec = cast(ModuleSpec, module.__spec__)
        filename = cast(str, spec.origin)
        source = Path(filename).read_text("utf-8")
        import_content(source, filename, module)


@contextmanager
def external_hook() -> Iterator[None]:
    hook = ExternalImporter()
    sys.meta_path.insert(0, hook)
    try:
        yield
    finally:
        del sys.meta_path[0]


@lru_cache
def _hook_typing() -> ModuleType:
    hook = ModuleType(typing.__name__)
    hook.__file__ = typing.__file__
    for attr in ["__file__", "List"]:
        setattr(hook, attr, getattr(typing, attr))
    return hook


def _hook__import__(
    name: str,
    globals_: Any,
    locals_: Any,
    fromlist: Optional[Sequence[str]],
    level: int,
) -> Any:
    if level == 0 and name in sys.modules:
        if name == "typing":
            return _hook_typing()
        ns, _, rest = name.partition(".")
        ig = {"__main__", "cli", "engine"}
        if ns == "ingraph":
            if not (
                (not rest and not (set(fromlist or set()) & ig))
                or (rest and rest.partition(".")[0] not in ig)
            ):
                raise ImportError("Unexpected import")
        else:
            spec = sys.modules[name].__spec__
            if spec is None or not isinstance(spec.loader, (ExternalImporter,)):
                raise ModuleNotFoundError(f"No module named {ns!r}")
    return __import__(name, globals_, locals_, fromlist, level)  # type: ignore
