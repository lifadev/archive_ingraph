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

import hashlib
import importlib.resources
import inspect
import os
import stat
import string
import tempfile
import zipfile
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass, field
from functools import partial, wraps
from pathlib import Path
from types import ModuleType
from typing import (IO, Any, Iterator, Mapping, NamedTuple, Optional, Sequence,
                    Set, Tuple, Type, Union)
from unittest.mock import sentinel

import networkx as nx
from more_itertools import pairwise

_NOVALUE = sentinel.NOVALUE
ROOT = ("_ig_root",)
_GRAPH: ContextVar[nx.Graph] = ContextVar("graph")
_NODE: ContextVar["Node"] = ContextVar("node")


def process(root: Type["ExternalResource"]) -> nx.Graph:
    with new_graph(root) as graph:
        root(**_getparmeters(root))
        return graph


class Location(NamedTuple):
    filename: str
    lines: Tuple[int, int]
    columns: Tuple[int, int]
    source: str


@dataclass(unsafe_hash=True)
class Node:
    lineage: Tuple[str, ...] = field(compare=True)
    name: str = field(compare=False)
    loc: "Location" = field(compare=False)
    resource: Optional[Any] = field(default=None, compare=False)
    assets: Set["Asset"] = field(default_factory=set, compare=False)

    def __repr__(self) -> str:
        return repr(self.lineage)


@contextmanager
def new_graph(root) -> Iterator[nx.Graph]:
    graph = nx.DiGraph()
    node = Node(
        lineage=ROOT,
        name="root",
        loc=Location(
            filename=root._ig_filename,
            lines=root._ig_lines,
            columns=root._ig_columns,
            source=root._ig_source,
        ),
    )
    graph.add_node(node)
    token_graph = _GRAPH.set(graph)
    token_node = _NODE.set(node)
    try:
        yield graph
    finally:
        _NODE.reset(token_node)
        _GRAPH.reset(token_graph)


@contextmanager
def new_node(name, loc) -> Iterator[Node]:
    graph = _GRAPH.get()
    parent = _NODE.get()
    node = Node(lineage=parent.lineage + (name,), name=name, loc=loc)
    graph.add_node(node)
    graph.add_edge(parent, node)
    token = _NODE.set(node)
    try:
        yield node
    finally:
        _NODE.reset(token)


class MetaStatic(type):
    def __instancecheck__(self, instance):
        return not hasattr(instance, "_ig_dynamic") and hasattr(instance, "_ig_value")


class Static(metaclass=MetaStatic):
    ...


def todynamic(value):
    if not isinstance(value, Static):
        return value
    res = type(value)(value._ig_value)
    res._ig_dynamic = True
    return res


class Boolean:
    _ig_hint = "boolean"

    def __init__(self, value=_NOVALUE):
        if value != _NOVALUE:
            if not isinstance(value, bool):
                raise TypeError("value is not a static boolean")
            self._ig_value = value

    def __repr__(self):
        return (
            "Boolean()"
            if not hasattr(self, "_ig_value")
            else f"Boolean(value={self._ig_value!r})"
        )


class Number:
    _ig_hint = "number"

    def __init__(self, value=_NOVALUE):
        if value != _NOVALUE:
            if not isinstance(value, (int, float)):
                raise TypeError("value is not a static number")
            self._ig_value = value

    def __int__(self):
        if not isinstance(self, Static):
            raise TypeError("number is not static")
        return int(self._ig_value)

    def __repr__(self):
        return (
            "Number()"
            if not hasattr(self, "_ig_value")
            else f"Number(value={self._ig_value!r})"
        )


class String:
    _ig_hint = "string"

    def __init__(self, value: str = _NOVALUE):
        if value != _NOVALUE:
            if not isinstance(value, str):
                raise TypeError("value is not a static string")
            self._ig_value = value

    def __add__(self, other):
        return String("").join(LISTS[String]([self, other]))

    def __repr__(self):
        return (
            "String()"
            if not hasattr(self, "_ig_value")
            else f"String(value={self._ig_value!r})"
        )

    def format(self, *args, **kwargs):
        if not isinstance(self, Static):
            raise TypeError("formatting string is not a static string")
        fmtr = Formatter()
        fmt = fmtr.vformat(self._ig_value, args, kwargs)
        return Sub(String(fmt), Map(fmtr.kwargs))

    def join(self, items) -> "Join":
        return Join(items, self)

    def replace(self, old, new) -> "Join":
        if not isinstance(new, String):
            raise TypeError("new is not a string")
        return new.join(self.split(old))

    def split(self, separator) -> "Split":
        return Split(self, separator)


class Formatter(string.Formatter):
    def __init__(self):
        self.kwargs = {}

    @staticmethod
    def ig_convert(value, conv):
        if conv is not None:
            raise TypeError("field conversion is not supported")
        return value

    @staticmethod
    def ig_format(value, spec):
        if spec != "":
            raise TypeError("format specification is not supported")
        return value

    @staticmethod
    def ig_map(value, kwargs):
        key = String(f"A{len(kwargs)}")
        key = next(iter(k for k, v in kwargs.items() if v == value), key)
        return f"${{{key._ig_value}}}", {key: value}

    def convert_field(self, value, conv):
        return self.ig_convert(value, conv)

    def format_field(self, value, spec):
        value = self.ig_format(value, spec)
        fmt, kwarg = self.ig_map(value, self.kwargs)
        self.kwargs.update(kwarg)
        return fmt


class AccountID(String):
    def __repr__(self):
        return f"{type(self).__name__}()"


class Base64Encoded(String):
    def __init__(self, target):
        if not isinstance(target, String):
            raise TypeError("target is not a string")
        self._ig_target = target

    def __repr__(self):
        return f"Base64Encoded(target={self._ig_target!r})"


class Join(String):
    def __init__(self, items, separator):
        if not isinstance(items, LISTS[String]):
            raise TypeError("items are not a list of strings")
        self._ig_items = items
        if not (isinstance(separator, Static) and isinstance(separator, String)):
            raise TypeError("separator is not a static string")
        self._ig_separator = separator

    def __repr__(self):
        return f"Join(items={self._ig_items!r}, separator={self._ig_separator!r})"


class Partition(String):
    def __repr__(self):
        return f"{type(self).__name__}()"


class Ref(String):
    def __init__(self, node):
        self._ig_node = node

    def __repr__(self):
        return f"Ref(node={self._ig_node!r})"


class Region(String):
    def __repr__(self):
        return f"{type(self).__name__}()"


class StackID(String):
    def __repr__(self):
        return f"{type(self).__name__}()"


class StackName(String):
    def __repr__(self):
        return f"{type(self).__name__}()"


class URLSuffix(String):
    def __repr__(self):
        return f"{type(self).__name__}()"


class Sub(String):
    def __init__(self, format, kwargs):
        if not (isinstance(format, Static) and isinstance(format, String)):
            raise TypeError("format is not a static string")
        self._ig_format = format
        if not (isinstance(kwargs, Static) and isinstance(kwargs, Map)):
            raise TypeError("kwargs is not a static map")
        if any(not isinstance(v, (Number, String)) for v in kwargs._ig_value.values()):
            raise TypeError("kwargs values are not only number or string")
        self._ig_kwargs = kwargs

    def __repr__(self):
        return f"Sub(format={self._ig_format!r}, kwargs={self._ig_kwargs!r})"


class Select:
    def __init__(self, items, index):
        if not isinstance(items, LISTS[self._ig_select_type]):
            raise TypeError(
                f"items are not a list of {self._ig_select_type.__name__.lower()}"
            )
        self._ig_items = items
        if not (isinstance(index, Static) and isinstance(index, Number)):
            raise TypeError("index is not a static number")
        self._ig_index = index

    def __repr__(self):
        name = f"List[{self._ig_select_type.__name__}]"
        return f"Select[{name}](items={self._ig_items!r}, index={self._ig_index!r})"


SELECTS = {
    t: type(Select.__name__, (Select, t), dict(_ig_select_type=t))
    for t in [Boolean, Number, String]
}


class ManagedList:
    def __init__(self, value=_NOVALUE):
        if value != _NOVALUE:
            if not (
                isinstance(value, list)
                and len(value) > 0
                and all(isinstance(v, self._ig_list_type) for v in value)
            ):
                raise TypeError(
                    f"value is not a static list of {self._ig_list_type.__name__.lower()}"
                )
            self._ig_value = value

    def __getitem__(self, index):
        if not (isinstance(index, Static) and isinstance(index, Number)):
            raise TypeError("index is not a static number")
        if hasattr(self, "_ig_value"):
            return todynamic(self._ig_value[int(index)])
        return SELECTS[self._ig_list_type](self, index)

    def __repr__(self):
        name = f"List[{self._ig_list_type.__name__}]"
        return (
            f"{name}()"
            if not hasattr(self, "_ig_value")
            else f"{name}(value={self._ig_value!r})"
        )


LISTS = {
    t: type(
        ManagedList.__name__,
        (ManagedList,),
        dict(_ig_list_type=t, _ig_hint=f"list of {t._ig_hint}"),
    )
    for t in [Boolean, Number, String]
}


class AvailabilityZones(LISTS[String]):
    def __repr__(self):
        return f"{type(self).__name__}()"


class CIDR(LISTS[String]):
    def __init__(self, *, block, count, bits):
        if not isinstance(block, String):
            raise TypeError("block is not a string")
        self._ig_block = block
        if not isinstance(count, Number):
            raise TypeError("count is not a number")
        self._ig_count = count
        if not isinstance(bits, Number):
            raise TypeError("bits is not a number")
        self._ig_bits = bits

    def __repr__(self):
        return (
            f"CIDR(block={self._ig_block!r}, count={self._ig_count!r},"
            f"bits={self._ig_bits!r})"
        )


class NotificationARNs(LISTS[String]):
    def __repr__(self):
        return f"{type(self).__name__}()"


class Split(LISTS[String]):
    def __init__(self, target, separator):
        if not isinstance(target, String):
            raise TypeError("target is not a string")
        self._ig_target = target
        if not (isinstance(separator, Static) and isinstance(separator, String)):
            raise TypeError("separator is not a static string")
        self._ig_separator = separator

    def __repr__(self):
        return f"Split(target={self._ig_target!r}, separator={self._ig_separator!r})"


class FreeList:
    def __init__(self, value):
        if not (
            isinstance(value, list)
            and len(value) > 0
            and not any(
                isinstance(v, (NativeResource, ExternalResource)) for v in value
            )
        ):
            raise TypeError("value is not a valid list")
        self._ig_value = value

    def __repr__(self):
        return f"List[*](value={self._ig_value!r})"


class NativeResourceList:
    def __init__(self, value):
        if not (
            isinstance(value, list)
            and len(value) > 0
            and all(isinstance(v, NativeResource) for v in value)
        ):
            raise TypeError("value is not a valid native resource list")
        self._ig_value = value

    def __repr__(self):
        return f"List[NativeResource](value={self._ig_value!r})"


def _common_ancestor(types):
    g = nx.DiGraph()
    for t in types:
        g.add_edges_from(pairwise(reversed(inspect.getmro(t))))
    while len(types) != 1:
        types, pairs = [], pairwise(types)
        for pair in pairs:
            types.append(nx.lowest_common_ancestor(g, *pair))
    return types[0]


def new_list(value):
    if not (isinstance(value, list) and len(value) > 0):
        raise TypeError("value is not a valid list")
    ancestor = _common_ancestor([type(v) for v in value])
    if ancestor in LISTS:
        return LISTS[ancestor](value)
    if issubclass(ancestor, NativeResource):
        return NativeResourceList(value)
    return FreeList(value)


class Map:
    def __init__(self, value=_NOVALUE):
        if value != _NOVALUE:
            if not (
                isinstance(value, dict)
                and all(
                    isinstance(k, Static) and isinstance(k, String)
                    for k in value.keys()
                )
                and not any(
                    isinstance(v, (NativeResource, ExternalResource))
                    for v in value.values()
                )
            ):
                raise TypeError("value is not a static map")
            self._ig_value = value

    def __repr__(self):
        return (
            "Map()"
            if not hasattr(self, "_ig_value")
            else f"Map(value={self._ig_value!r})"
        )


class Parameter:
    def __init__(self, name, default):
        self._ig_name = name
        self._ig_default = default

    def __repr__(self):
        name = f"Parameter[{self._ig_param_type.__name__}]"
        return f"{name}(name={self._ig_name!r}, default={self._ig_default!r})"


PARAMETERS = {
    t: type(Parameter.__name__, (Parameter, t), dict(_ig_param_type=t))
    for t in [Number, LISTS[Number], String, LISTS[String]]
}


class Attribute:
    def __init__(self, node, name):
        self._ig_node = node
        self._ig_name = name

    def __repr__(self):
        name = f"Attribute[{self._ig_attr_type.__name__}]"
        return f"{name}(node={self._ig_node!r}, name={self._ig_name!r})"


ATTRIBUTES = {
    t: type(Attribute.__name__, (Attribute, t), dict(_ig_attr_type=t))
    for t in [Boolean, LISTS[Boolean], Number, LISTS[Number], String, LISTS[String]]
}


class Property:
    def __init_subclass__(cls, *, module, params):
        super().__init_subclass__()
        cls.__module__ = module
        cls.__signature__ = _makesig(params)

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        self._ig_data = {k: v for k, v in bound.arguments.items()}

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
            return
        raise AttributeError(f"property is read-only")


class NativeResource:
    def __init_subclass__(cls, *, module, kind, attrs, params):
        cls.__module__ = module
        cls.__annotations__ = {k: _frompytype(v) for k, v in attrs.items()}
        relax = kind == "AWS::CloudFormation::CustomResource"
        cls.__signature__ = _makesig(params, kwargs=relax)
        cls._ig_kind = kind

    def __init__(self, *args, _ig_node, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        deps = bound.arguments.pop("DependsOn", None)
        if deps is not None and not isinstance(deps, NativeResourceList):
            raise TypeError("DependsOn is not a list of native resources")
        self._ig_deps = getattr(deps, "_ig_value", [])
        self._ig_node = _ig_node
        _ig_node.resource = self
        kwargs = bound.arguments.pop("kwargs", {})
        self._ig_data = {k: v for k, v in bound.arguments.items()}
        self._ig_data.update(kwargs)

    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
            return
        raise AttributeError(f"native resource is read-only")

    def __getattribute__(self, name):
        if name.startswith("_"):
            return super().__getattribute__(name)
        if name == "Ref":
            return Ref(self._ig_node)
        if name in self.__annotations__:
            return ATTRIBUTES[self.__annotations__[name]](self._ig_node, name)
        return super().__getattribute__(name)


def _makesig(params, kwargs=False):
    items = [
        inspect.Parameter(
            name,
            inspect.Parameter.KEYWORD_ONLY,
            default=inspect.Parameter.empty if required else _NOVALUE,
        )
        for name, required in params
    ]
    if kwargs:
        items.append(inspect.Parameter("kwargs", inspect.Parameter.VAR_KEYWORD))
    return inspect.Signature(items)


class CustomResource:
    def __init_subclass__(cls):
        _check_custom_defn(cls)
        _check_output(cls)
        parent = cls.__bases__[-1]
        attrs = cls.__annotations__
        super().__init_subclass__(
            module=parent.__module__, kind=parent._ig_kind, attrs={}, params={}
        )
        cls.__annotations__ = {k: _frompytype(v) for k, v in attrs.items()}
        cls.__signature__ = parent.__signature__


def _check_custom_defn(cls):
    from ingraph.aws import aws_cloudformation

    if cls.__bases__ != (CustomResource, aws_cloudformation.CustomResource):
        raise TypeError(
            f"{cls.__name__!r} can only inherit "
            "from 'aws_cloudformation.CustomResource'"
        )

    keys = {"__annotations__", "__doc__", "__module__"}

    for k in cls.__dict__.keys():
        if not (k in keys or k.startswith("_ig_")):
            raise TypeError(f"{cls.__name__!r} level {k!r} is not valid")


class ExternalResource:
    def __init_subclass__(cls):
        _check_defn(cls)
        _check_input(cls)
        _check_output(cls)
        _proxy_init(cls)
        super().__init_subclass__()

    def __setattr__(self, name, value):
        if name.startswith("_"):  # pragma: no cover
            super().__setattr__(name, value)
            return
        anns = getattr(self, "__annotations__", {})
        if name not in anns:
            raise AttributeError(f"attribute {name!r} doesn't exist")
        if name in self.__dict__:
            raise AttributeError(f"attribute {name!r} is read-only")
        typ = _frompytype(anns[name])
        if not isinstance(value, typ):
            raise TypeError(f"value is not a {typ._ig_hint}")
        super().__setattr__(name, value)

    def __init__(self, *, _ig_node):
        self._ig_node = _ig_node
        _ig_node.resource = self

    def __getattribute__(self, name):
        res = super().__getattribute__(name)
        return res if name.startswith("_") else todynamic(res)


def _check_defn(cls):
    keys = {"__annotations__", "__doc__", "__init__", "__module__"}

    if "__init__" not in cls.__dict__:
        raise TypeError("'__init__' method not found")

    for k in cls.__dict__.keys():
        if not (k in keys or k.startswith("_ig_")):
            raise TypeError(f"{cls.__name__!r} level {k!r} is not valid")


def _check_input(cls):
    from typing import List

    params = {
        k: v
        for k, v in inspect.signature(cls.__init__).parameters.items()
        if not k.startswith("_")
    }

    if (
        len(params) == 0
        or list(params)[0] != "self"
        or params["self"].kind != inspect.Parameter.POSITIONAL_OR_KEYWORD
    ):
        raise TypeError("first positional argument must be 'self'")
    params.pop("self")

    variadic = {inspect.Parameter.VAR_KEYWORD, inspect.Parameter.VAR_POSITIONAL}
    if any(p.kind in variadic for p in params.values()):
        raise TypeError("variadic parameters are not supported")

    positional = {
        inspect.Parameter.POSITIONAL_ONLY,
        inspect.Parameter.POSITIONAL_OR_KEYWORD,
    }
    if any(p.kind in positional for p in params.values()):
        raise TypeError("positional parameters are not supported")

    if len(params) > 60:
        raise TypeError("maximum number of parameters (60) exceeded")

    typs = {int, float, str, List[int], List[float], List[str]}
    for name, param in params.items():
        if len(name.replace("_", "")) > 255:
            raise TypeError(f"parameter is too long")
        typ = param.annotation
        if typ is inspect.Parameter.empty:
            raise TypeError(f"parameter {name!r} has no type")
        if typ not in typs:
            raise TypeError(f"parameter {name!r} type is invalid")
        typ = _frompytype(typ)
        defl = param.default
        if defl is not inspect.Parameter.empty:
            if not (isinstance(defl, Static) and isinstance(defl, typ)) or (
                issubclass(typ, ManagedList)
                and not all(isinstance(v, Static) for v in defl._ig_value)
            ):
                raise TypeError(
                    f"parameter {name!r} default value is not a static {typ._ig_hint}"
                )


def _check_output(cls):
    from typing import Final

    attrs = {
        k: v
        for k, v in getattr(cls, "__annotations__", {}).items()
        if not k.startswith("_")
    }

    if len(attrs) > 60:
        raise TypeError("maximum number of attributes (60) exceeded")

    typs = {int, float, str, Final[int], Final[float], Final[str]}
    for name, ann in attrs.items():
        if len(name.replace("_", "")) > 255:
            raise TypeError(f"attribute is too long")
        if ann not in typs:
            raise TypeError(f"attribute {name!r} type is invalid")


def _proxy_init(cls):
    wrapped = cls.__init__
    params = {
        k: v
        for k, v in inspect.signature(wrapped).parameters.items()
        if not k.startswith("_")
    }
    params.pop("self")
    attrs = {
        k: _frompytype(v)
        for k, v in getattr(cls, "__annotations__", {}).items()
        if not k.startswith("_")
    }

    @wraps(wrapped)
    def wrapper(self, *, _ig_node=None, **kwargs):
        res = {}
        for k, v in params.items():
            if k in kwargs:
                arg = todynamic(kwargs[k])
            elif v.default is not inspect.Parameter.empty:
                arg = todynamic(v.default)
            else:  # pragma: no cover
                continue
            typ = _frompytype(v.annotation)
            if not isinstance(arg, typ):
                raise TypeError(f"argument {k!r} is not a {typ._ig_hint}")
            res[k] = arg
        _ig_node = _ig_node if _ig_node is not None else _NODE.get()
        super(cls, self).__init__(_ig_node=_ig_node)
        wrapped(self, **res)
        for k, v in attrs.items():
            if k not in self.__dict__:
                raise AttributeError(f"attribute {k!r} not initialized")

    cls.__init__ = wrapper


def getparameters(graph: nx.Graph) -> Mapping[str, Parameter]:
    root = next(n for n in graph.nodes() if n.lineage == ROOT)
    return _getparmeters(root.resource)


def _getparmeters(cls):
    return {
        k: PARAMETERS[_frompytype(v.annotation)](
            k, None if v.default is inspect.Parameter.empty else v.default
        )
        for k, v in inspect.signature(cls.__init__).parameters.items()
        if not (k.startswith("_") or k == "self")
    }


def getoutputs(graph: nx.Graph) -> Mapping[str, Any]:
    root = next(n for n in graph.nodes() if n.lineage == ROOT)
    anns = getattr(root.resource, "__annotations__", {})
    return {k: getattr(root.resource, k) for k in anns.keys()}


def _frompytype(typ):
    from typing import Final, List

    return {
        bool: Boolean,
        int: Number,
        float: Number,
        str: String,
        List[bool]: LISTS[Boolean],
        List[int]: LISTS[Number],
        List[float]: LISTS[Number],
        List[str]: LISTS[String],
    }[
        {
            Final[bool]: bool,
            Final[int]: int,
            Final[float]: float,
            Final[str]: str,
            Final[List[bool]]: List[bool],
            Final[List[int]]: List[int],
            Final[List[float]]: List[float],
            Final[List[str]]: List[str],
        }.get(typ, typ)
    ]


class Asset:
    _ig_path: Path
    _ig_hash: str
    _ig_compressed: bool

    def __init__(
        self,
        *,
        name: String,
        package: Optional[ModuleType] = None,
        compress: Optional[Boolean] = None,
    ):
        if not (isinstance(name, Static) and isinstance(name, String)):
            raise TypeError("asset name is not a static string")
        name_ = name._ig_value
        compress_ = False
        if compress is not None:
            if not (isinstance(compress, Static) and isinstance(compress, Boolean)):
                raise TypeError("asset compress is not a static boolean")
            compress_ = compress._ig_value
        if len(Path(name_).parts) > 1:
            raise ValueError("asset name includes path parts")
        if package is None:
            package = getattr(
                inspect.getmodule(inspect.stack()[2][0]), "__package__", None
            )
        if package is None:
            path = Path(inspect.getfile(inspect.stack()[2][0])).parent / name_
            self._process(path, compress_)
        else:
            with importlib.resources.path(package, name_) as path:
                self._process(path, compress_)

    def _process(self, path: Path, compress: bool) -> None:
        path = path.resolve()
        if compress:
            file = package_zip(path)
            path = Path(file.name)
        self._ig_path = path
        self._ig_hash = gethash(path)
        self._ig_compressed = compress

    @property
    def bucket(self) -> "AssetBucket":
        _NODE.get().assets.add(self)
        return AssetBucket(self)

    @property
    def key(self) -> "AssetKey":
        _NODE.get().assets.add(self)
        return AssetKey(self)

    @property
    def text(self) -> String:
        if self._ig_compressed:
            raise TypeError("cannot retrieve text content from compressed asset")
        return String(self._ig_path.read_text())

    @property
    def uri(self) -> "AssetURI":
        _NODE.get().assets.add(self)
        return AssetURI(self)

    @property
    def url(self) -> "AssetURL":
        _NODE.get().assets.add(self)
        return AssetURL(self)

    def __repr__(self) -> str:
        return repr(str(self._ig_path))

    def __hash__(self) -> int:
        return hash(self._ig_hash)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Asset):  # pragma: no cover
            return NotImplemented
        return self._ig_hash == other._ig_hash


class AssetAttribute(String):
    def __init__(self, asset: Asset):
        self._ig_asset = asset


class AssetBucket(AssetAttribute):
    ...


class AssetKey(AssetAttribute):
    ...


class AssetURI(AssetAttribute):
    ...


class AssetURL(AssetAttribute):
    ...


def package_zip(path: Path, select: Optional[Sequence[Path]] = None) -> IO[bytes]:
    paths: List[Path] = []
    cwd = Path.cwd()
    if path.is_dir():
        if select is not None:
            paths = list(select)
        else:
            paths = list(sorted(p.relative_to(path) for p in path.glob("**/[!.]*")))
        os.chdir(path)
    else:
        paths = [path.relative_to(path.parent)]
        os.chdir(path.parent)
    file = tempfile.NamedTemporaryFile(mode="wb", suffix=".zip", delete=False)
    epoch = (2013, 2, 21, 0, 0, 0)
    with zipfile.ZipFile(file, "w") as zip_file:
        for path in paths:
            perm = 0o555 if os.access(path, os.X_OK) else 0o444
            if path.is_file() and not path.is_symlink():
                info = zipfile.ZipInfo(filename=str(path), date_time=epoch)
                info.external_attr = (stat.S_IFREG | perm) << 16
                zip_file.writestr(  # type: ignore
                    info,
                    path.read_bytes(),
                    compress_type=zipfile.ZIP_DEFLATED,
                    compresslevel=9,
                )
            else:
                info = zipfile.ZipInfo(filename=str(path) + "/", date_time=epoch)
                info.external_attr = (stat.S_IFDIR | perm) << 16
                zip_file.writestr(info, "\x00", compress_type=zipfile.ZIP_STORED)
    os.chdir(cwd)
    return file


def gethash(data: Union[Path, IO[bytes]]) -> str:
    if isinstance(data, Path):
        with data.open("rb") as file:
            return _gethash(file)
    return _gethash(data)


def _gethash(reader: IO[bytes]) -> str:
    hasher = hashlib.sha1()
    for block in iter(partial(reader.read, 65536), b""):
        hasher.update(block)
    return hasher.hexdigest()
