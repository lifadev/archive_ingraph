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


import inspect
import textwrap

import pytest

from ingraph.engine import importer
from ingraph.engine.core import (ATTRIBUTES, CIDR, LISTS, PARAMETERS, SELECTS,
                                 AccountID, Asset, Attribute,
                                 AvailabilityZones, Base64Encoded, Boolean,
                                 CustomResource, ExternalResource, FreeList,
                                 Join, ManagedList, Map, NativeResource,
                                 NativeResourceList, NotificationARNs, Number,
                                 Parameter, Partition, Property, Ref, Region,
                                 Select, Split, StackID, StackName, Static,
                                 String, Sub, URLSuffix, _getparmeters,
                                 new_list)


class _NATIVE(NativeResource, module="mock", kind="mock", attrs={}, params=[]):
    ...


class _EXTERNAL(ExternalResource):
    def __init__(self):
        ...


@pytest.mark.parametrize(
    "typ,value,error",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            ("boolean", Boolean, "True", "value is not a static boolean"),
            ("number", Number, "42", "value is not a static number"),
            ("string", String, 42, "value is not a static string"),
            (
                "list[boolean]_empty",
                LISTS[Boolean],
                [],
                "value is not a static list of boolean",
            ),
            (
                "list[boolean]",
                LISTS[Boolean],
                [True, "False"],
                "value is not a static list of boolean",
            ),
            (
                "list[number]_empty",
                LISTS[Number],
                [],
                "value is not a static list of number",
            ),
            (
                "list[number]",
                LISTS[Number],
                [42, "42"],
                "value is not a static list of number",
            ),
            (
                "list[string]_empty",
                LISTS[String],
                [],
                "value is not a static list of string",
            ),
            (
                "list[string]",
                LISTS[String],
                ["foo", 42],
                "value is not a static list of string",
            ),
            ("list[*]_empty", FreeList, [], "value is not a valid list"),
            (
                "list[*]_native",
                FreeList,
                lambda node: [_NATIVE(_ig_node=node)],
                "value is not a valid list",
            ),
            (
                "list[*]_ext",
                FreeList,
                lambda node: [_EXTERNAL(_ig_node=node)],
                "value is not a valid list",
            ),
            (
                "list[native]_empty",
                NativeResourceList,
                [],
                "value is not a valid native resource list",
            ),
            (
                "list[native]_ext",
                NativeResourceList,
                lambda node: [_EXTERNAL(_ig_node=node)],
                "value is not a valid native resource list",
            ),
            ("map_key", Map, {String(): Number()}, "value is not a static map"),
            (
                "map_value_native",
                Map,
                lambda node: ({String(""): _NATIVE(_ig_node=node)}),
                "value is not a static map",
            ),
            (
                "map_value_ext",
                Map,
                lambda node: ({String(""): _EXTERNAL(_ig_node=node)}),
                "value is not a static map",
            ),
        ]
    ],
)
def test_static_check(typ, value, error, mocker):
    node = mocker.sentinel.NODE
    with pytest.raises(TypeError, match=error):
        typ(value(node) if inspect.isfunction(value) else value)


@pytest.mark.parametrize(
    "value,dynamic",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            ("boolean_static", Boolean(True), False),
            ("boolean_dynamic", Boolean(), True),
            ("number_static", Number(42), False),
            ("number_dynamic", Number(), True),
            ("string_static", String("foo"), False),
            ("string_dynamic", String(), True),
            (
                "list[boolean]_static",
                LISTS[Boolean]([Boolean(True), Boolean()]),
                False,
            ),
            ("list[boolean]_dynamic", LISTS[Boolean](), True),
            ("list[number]_static", LISTS[Number]([Number(4), Number()]), False,),
            ("list[number]_dynamic", LISTS[Number](), True),
            ("list[string]_static", LISTS[String]([String("foo"), String()]), False,),
            ("list[string]_dynamic", LISTS[String](), True),
            (
                "map_static",
                Map({String("foo"): Number(), String("bar"): Boolean(True),}),
                False,
            ),
            ("list[*]", FreeList([LISTS[String](), String()]), False),
            (
                "list[native]",
                lambda node: NativeResourceList([_NATIVE(_ig_node=node)]),
                False,
            ),
            ("map_dynamic", Map(), True),
        ]
    ],
)
def test_types(value, dynamic, mocker):
    node = mocker.sentinel.NODE
    value = value(node) if inspect.isfunction(value) else value
    if dynamic:
        assert not isinstance(value, Static)
    else:
        assert isinstance(value, Static)
        setattr(value, "_ig_dynamic", True)
        assert not isinstance(value, Static)


def test_number_int():
    with pytest.raises(TypeError, match="number is not static"):
        int(Number())

    assert int(Number(42)) == 42


@pytest.mark.parametrize(
    "left,right",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            ("static", String("foo"), String("bar")),
            ("dynamic", String(), String()),
            ("mixed", String("foo"), String()),
        ]
    ],
)
def test_string_add(left, right):
    res = left + right
    assert isinstance(res, String)
    assert isinstance(res, Join)
    assert not isinstance(res, Static)


def test_string_join_check():
    with pytest.raises(TypeError):
        String().join(LISTS[String]())


@pytest.mark.parametrize(
    "items",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            ("static", LISTS[String]([String("foo"), String("bar")])),
            ("dynamic", LISTS[String]()),
            ("mixed", LISTS[String]([String("foo"), String()])),
        ]
    ],
)
def test_string_join(items):
    res = String("baz").join(items)
    assert isinstance(res, String)
    assert isinstance(res, Join)
    assert not isinstance(res, Static)


@pytest.mark.parametrize(
    "target",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [("static", String("foo")), ("dynamic", String()),]
    ],
)
def test_string_replace_check(target):
    with pytest.raises(TypeError, match="new is not a string"):
        target.replace(String("f"), None)

    with pytest.raises(TypeError, match="separator is not a static string"):
        target.replace(String(), String("-"))

    with pytest.raises(TypeError, match="separator is not a static string"):
        target.replace(String("-"), String())


@pytest.mark.parametrize(
    "target",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [("static", String("foo")), ("dynamic", String()),]
    ],
)
def test_string_replace(target):
    res = target.replace(String("-"), String("+"))
    assert isinstance(res, String)
    assert isinstance(res, Join)
    assert not isinstance(res, Static)


@pytest.mark.parametrize(
    "target",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [("static", String("foo")), ("dynamic", String()),]
    ],
)
def test_string_split_check(target):
    with pytest.raises(TypeError, match="separator is not a static string"):
        target.split(String())


@pytest.mark.parametrize(
    "target",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [("static", String("foo")), ("dynamic", String()),]
    ],
)
def test_string_split(target):
    res = target.split(String("-"))
    assert isinstance(res, LISTS[String])
    assert isinstance(res, Split)
    assert not isinstance(res, Static)


def test_string_format_check():
    with pytest.raises(TypeError, match="formatting string is not a static string"):
        String().format()

    with pytest.raises(TypeError, match="field conversion is not supported"):
        String("{!r}").format(String())

    with pytest.raises(TypeError, match="format specification is not supported"):
        String("{:>3}").format(String())

    with pytest.raises(ValueError, match="cannot switch from manual field"):
        String("{0} {}").format(String())


def test_string_format():
    res = String("{} {foo} {foo}").format(String("bar"), foo=Number())
    assert isinstance(res, Sub)
    assert isinstance(res, String)
    assert not isinstance(res, Static)
    assert res._ig_format._ig_value == "${A0} ${A1} ${A1}"
    assert len(res._ig_kwargs._ig_value) == 2


def test_base64encoded_check():
    with pytest.raises(TypeError, match="target is not a string"):
        Base64Encoded(None)


@pytest.mark.parametrize(
    "target",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [("static", String("foo")), ("dynamic", String()),]
    ],
)
def test_base64encoded(target):
    res = Base64Encoded(target)
    assert isinstance(res, String)
    assert isinstance(res, Base64Encoded)
    assert not isinstance(res, Static)


def test_join_check():
    with pytest.raises(TypeError, match="items are not a list of strings"):
        Join(LISTS[Boolean](), String("-"))

    with pytest.raises(TypeError, match="separator is not a static string"):
        Join(LISTS[String](), String())


@pytest.mark.parametrize(
    "items",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            ("static", LISTS[String]([String("foo"), String("bar")]),),
            ("dynamic", LISTS[String]()),
            ("mixed", LISTS[String]([String("foo"), String()])),
        ]
    ],
)
def test_join(items):
    res = Join(items, String("-"))
    assert isinstance(res, Join)
    assert isinstance(res, String)
    assert not isinstance(res, Static)


def test_ref():
    res = Ref("mock")
    assert isinstance(res, String)
    assert not isinstance(res, Static)


def test_sub_check():
    with pytest.raises(TypeError, match="format is not a static string"):
        Sub(String(), Map({}))

    with pytest.raises(TypeError, match="kwargs is not a static map"):
        Sub(String("foo"), Map())

    err = "kwargs values are not only number or string"
    with pytest.raises(TypeError, match=err):
        Sub(String("foo"), Map({String("foo"): Boolean()}))


def test_sub():
    res = Sub(String("foo"), Map({}))
    assert isinstance(res, Sub)
    assert isinstance(res, String)
    assert not isinstance(res, Static)


@pytest.mark.parametrize(
    "typ",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [("boolean", Boolean), ("number", Number), ("string", String),]
    ],
)
def test_select_check(typ):
    hint = typ.__name__.lower()
    with pytest.raises(TypeError, match=f"items are not a list of {hint}"):
        SELECTS[typ](None, Number(42))

    with pytest.raises(TypeError, match=f"index is not a static number"):
        SELECTS[typ](LISTS[typ](), Number())


@pytest.mark.parametrize(
    "typ,items",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            (
                "boolean_static",
                Boolean,
                LISTS[Boolean]([Boolean(True), Boolean(False)]),
            ),
            ("boolean_dynamic", Boolean, LISTS[Boolean]()),
            ("boolean_mixed", Boolean, LISTS[Boolean]([Boolean(True), Boolean()])),
            ("number_static", Number, LISTS[Number]([Number(4), Number(2)])),
            ("number_dynamic", Number, LISTS[Number]()),
            ("number_mixed", Number, LISTS[Number]([Number(42), Number()])),
            ("string_static", String, LISTS[String]([String("foo"), String("bar")])),
            ("number_dynamic", String, LISTS[String]()),
            ("number_mixed", String, LISTS[String]([String("foo"), String()])),
        ]
    ],
)
def test_select(typ, items):
    select = SELECTS[typ](items, Number(42))
    assert isinstance(select, SELECTS[typ])
    assert isinstance(select, typ)
    assert not isinstance(select, Static)


def test_selects():
    for k, v in SELECTS.items():
        assert issubclass(v, k)
        assert issubclass(v, Select)


@pytest.mark.parametrize(
    "target",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            ("boolean", LISTS[Boolean]()),
            ("number", LISTS[Number]()),
            ("string", LISTS[String]()),
        ]
    ],
)
def test_list_index_check(target):
    with pytest.raises(TypeError, match="index is not a static number"):
        target[Number()]


@pytest.mark.parametrize(
    "target,typ",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            ("boolean_static", LISTS[Boolean]([Boolean(True), Boolean()]), Boolean),
            ("boolean_dynamic", LISTS[Boolean](), SELECTS[Boolean]),
            ("number_static", LISTS[Number]([Number(42), Number()]), Number),
            ("number_dynamic", LISTS[Number](), SELECTS[Number]),
            ("string_static", LISTS[String]([String("foo"), String()]), String),
            ("string_dynamic", LISTS[String](), SELECTS[String]),
        ]
    ],
)
def test_list_index(target, typ):
    for i in range(0, 2):
        res = target[Number(i)]
        assert isinstance(res, typ)
        assert not isinstance(res, Static)


def test_lists():
    for k, v in LISTS.items():
        assert issubclass(v, ManagedList)
        assert not issubclass(v, k)


def test_cidr_check():
    with pytest.raises(TypeError, match="block is not a string"):
        CIDR(block=None, count=Number(), bits=Number())

    with pytest.raises(TypeError, match="count is not a number"):
        CIDR(block=String(), count=None, bits=Number())

    with pytest.raises(TypeError, match="bits is not a number"):
        CIDR(block=String(), count=Number(), bits=None)


@pytest.mark.parametrize(
    "block,count,bits",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            ("static", String("foo"), Number(4), Number(2)),
            ("dynamic", String(), Number(), Number()),
        ]
    ],
)
def test_cidr(block, count, bits):
    res = CIDR(block=block, count=count, bits=bits)
    assert isinstance(res, LISTS[String])
    assert isinstance(res, CIDR)
    assert not isinstance(res, Static)


def test_split_check():
    with pytest.raises(TypeError, match="target is not a string"):
        Split(Number(), String("-"))

    with pytest.raises(TypeError, match="separator is not a static string"):
        Split(String(), String())


@pytest.mark.parametrize(
    "target",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [("static", String("foo")), ("dynamic", String()),]
    ],
)
def test_split(target):
    res = Split(target, String("-"))
    assert isinstance(res, Split)
    assert isinstance(res, LISTS[String])
    assert not isinstance(res, Static)


def test_new_list_check():
    with pytest.raises(TypeError, match="value is not a valid list"):
        new_list(None)


@pytest.mark.parametrize(
    "value,typ",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            ("boolean", [Boolean()], LISTS[Boolean]),
            ("number", [Number()], LISTS[Number]),
            ("string", [String()], LISTS[String]),
            ("native", lambda node: [_NATIVE(_ig_node=node)], NativeResourceList,),
            ("free", [LISTS[String](), String()], FreeList),
        ]
    ],
)
def test_new_list(value, typ, mocker):
    node = mocker.sentinel.NODE
    value = value(node) if inspect.isfunction(value) else value
    res = new_list(value)
    assert isinstance(res, typ)


@pytest.mark.parametrize(
    "value,typ",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            ("account_id", AccountID(), String),
            ("availability_zones", AvailabilityZones(), LISTS[String]),
            ("notification_arns", NotificationARNs(), LISTS[String]),
            ("partition", Partition(), String),
            ("region", Region(), String),
            ("stack_id", StackID(), String),
            ("stack_name", StackName(), String),
            ("url_suffix", URLSuffix(), String),
        ]
    ],
)
def test_pseudo(value, typ):
    assert isinstance(value, typ)
    assert not isinstance(value, Static)


def test_parameters():
    for k, v in PARAMETERS.items():
        assert issubclass(v, Parameter)
        assert issubclass(v, k)

        res = v("mock", "kcom")
        assert isinstance(res, k)
        assert not isinstance(res, Static)


def test_attributes():
    for k, v in ATTRIBUTES.items():
        assert issubclass(v, Attribute)
        assert issubclass(v, k)

        res = v("mock", "kcom")
        assert isinstance(res, k)
        assert not isinstance(res, Static)


def test_property_params():
    class Foo(Property, module="MODULE", params=[("bar", False), ("baz", True)]):
        ...

    err = "missing a required argument: 'baz'"
    with pytest.raises(TypeError, match=err):
        Foo()

    err = "got an unexpected keyword argument 'qux'"
    with pytest.raises(TypeError, match=err):
        Foo(bar="BAR", baz="BAZ", qux=42)

    foo = Foo(baz="BAZ")
    assert foo._ig_data == {"baz": "BAZ"}
    assert foo.__module__ == "MODULE"

    foo = Foo(bar="BAR", baz="BAZ")
    assert foo._ig_data == {"bar": "BAR", "baz": "BAZ"}


def test_property_immut():
    class Foo(Property, module="MODULE", params=[]):
        ...

    foo = Foo()
    err = "property is read-only"
    with pytest.raises(AttributeError, match=err):
        foo.bar = 42


def test_native_deps(mocker):
    node = mocker.sentinel.NODE

    class Foo(
        NativeResource,
        module="MODULE",
        kind="KIND",
        attrs={},
        params=[("DependsOn", False)],
    ):
        ...

    err = "DependsOn is not a list of native resources"
    with pytest.raises(TypeError, match=err):
        Foo(_ig_node=node, DependsOn=42)

    bar = _NATIVE(_ig_node=node)
    foo = Foo(_ig_node=node, DependsOn=NativeResourceList([bar]))
    assert foo._ig_deps[0] == bar


def test_native_params(mocker):
    node = mocker.sentinel.NODE

    class Foo(
        NativeResource,
        module="MODULE",
        kind="KIND",
        attrs={},
        params=[("bar", False), ("baz", True)],
    ):
        ...

    err = "missing a required argument: 'baz'"
    with pytest.raises(TypeError, match=err):
        Foo(_ig_node=node)

    err = "got an unexpected keyword argument 'qux'"
    with pytest.raises(TypeError, match=err):
        Foo(_ig_node=node, bar="BAR", baz="BAZ", qux=42)

    foo = Foo(_ig_node=node, baz="BAZ")
    assert foo._ig_data == {"baz": "BAZ"}
    assert foo.__module__ == "MODULE"
    assert foo._ig_kind == "KIND"

    foo = Foo(_ig_node=node, bar="BAR", baz="BAZ")
    assert foo._ig_data == {"bar": "BAR", "baz": "BAZ"}


def test_native_immut(mocker):
    node = mocker.sentinel.NODE

    class Foo(NativeResource, module="MODULE", kind="KIND", attrs={}, params=[]):
        ...

    foo = Foo(_ig_node=node)
    err = "resource is read-only"
    with pytest.raises(AttributeError, match=err):
        foo.bar = 42


def test_native_attrs(mocker):
    from typing import List

    node = mocker.sentinel.NODE
    attrs = dict(
        a1=bool,
        a2=int,
        a3=float,
        a4=str,
        a5=List[bool],
        a6=List[int],
        a7=List[float],
        a8=List[str],
    )

    class Foo(NativeResource, module="MODULE", kind="KIND", attrs=attrs, params=[]):
        ...

    foo = Foo(_ig_node=node)

    assert isinstance(foo.Ref, Ref)
    for k, v in attrs.items():
        assert isinstance(getattr(foo, k), Attribute)


def test_custom_resource_bases():
    err = "'Foo' can only inherit from 'aws_cloudformation.CustomResource'"
    with pytest.raises(TypeError, match=err):
        with importer.aws_hook():

            class Foo(CustomResource, str):
                ...


def test_custom_resource_init():
    err = "Foo' level '__init__' is not valid"
    with pytest.raises(TypeError, match=err):
        with importer.aws_hook():
            from ingraph.aws import aws_cloudformation

            class Foo(CustomResource, aws_cloudformation.CustomResource):
                def __init__(self):
                    ...


def test_custom_resource_params(mocker):
    node = mocker.sentinel.NODE
    with importer.aws_hook():
        from ingraph.aws import aws_cloudformation

        class Foo(CustomResource, aws_cloudformation.CustomResource):
            Attr: int

        foo = Foo(_ig_node=node, ServiceToken="st", bar="BAR", baz=42)

    assert foo._ig_data == {"ServiceToken": "st", "bar": "BAR", "baz": 42}


def test_external_definition():
    with pytest.raises(TypeError, match="'__init__' method not found"):

        class Foo(ExternalResource):
            ...

    err = "'Foo' level 'bar' is not valid"
    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            bar = 1

            def __init__(self):
                ...

    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            bar: int = 1

            def __init__(self):
                ...

    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            def __init__(self):
                ...

            def bar():
                ...


def test_external_self():
    err = "first positional argument must be 'self'"
    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            def __init__():
                ...

    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            def __init__(fles):
                ...

    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            def __init__(*, self):
                ...


def test_external_variadic():
    err = "variadic parameters are not supported"
    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            def __init__(self, *args):
                ...

    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            def __init__(self, **kwargs):
                ...


def test_external_positional():
    err = "positional parameters are not supported"
    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            def __init__(self, foo):
                ...


def test_external_maxparams():
    params = ",".join([f"p{i}: int" for i in range(0, 61)])
    src = textwrap.dedent(
        f"""
    class Foo(ExternalResource):
        def __init__(self, *, {params}): ...
    """
    )

    err = r"maximum number of parameters \(60\) exceeded"
    with pytest.raises(TypeError, match=err):
        exec(compile(src, "<test>", "exec"))


def test_external_maxparamlen():
    param = f"{'p' * 256}: int"
    src = textwrap.dedent(
        f"""
    class Foo(ExternalResource):
        def __init__(self, *, {param}): ...
    """
    )

    err = "parameter is too long"
    with pytest.raises(TypeError, match=err):
        exec(compile(src, "<test>", "exec"))


def test_external_paramtype():
    err = "parameter 'bar' has no type"
    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            def __init__(self, *, bar):
                ...

    err = "parameter 'bar' type is invalid"
    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            def __init__(self, *, bar: bool):
                ...


def test_external_paramtypes():
    from typing import List

    class Foo(ExternalResource):
        def __init__(
            self,
            *,
            p1: int,
            p1d: int = Number(42),
            p2: float,
            p2d: float = Number(42.42),
            p3: str,
            p3d: str = String("foo"),
            p4: List[int],
            p4d: List[int] = LISTS[Number]([Number(42)]),
            p5: List[float],
            p5d: List[float] = LISTS[Number]([Number(42.42)]),
            p6: List[str],
            p6d: List[str] = LISTS[String]([String("foo")]),
        ):
            ...


def test_external_dynparam():
    err = "parameter 'bar' default value is not a static string"
    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            def __init__(self, *, bar: str = String()):
                ...

    from typing import List

    err = "parameter 'bar' default value is not a static list of string"
    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            def __init__(self, *, bar: List[str] = LISTS[String]()):
                ...

    err = "parameter 'bar' default value is not a static list of string"
    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            def __init__(self, *, bar: List[str] = LISTS[String]([String()])):
                ...


def test_external_maxattrs():
    attrs = "\n        ".join([f"a{i}: int" for i in range(0, 61)])
    src = textwrap.dedent(
        f"""
    class Foo(ExternalResource):
        {attrs}

        def __init__(self): ...
    """
    )

    err = r"maximum number of attributes \(60\) exceeded"
    with pytest.raises(TypeError, match=err):
        exec(compile(src, "<test>", "exec"))


def test_external_maxattrlen():
    attr = f"{'a' * 256}: int"
    src = textwrap.dedent(
        f"""
    class Foo(ExternalResource):
        {attr}

        def __init__(self): ...
    """
    )

    err = "attribute is too long"
    with pytest.raises(TypeError, match=err):
        exec(compile(src, "<test>", "exec"))


def test_external_attrtype():
    from typing import List

    err = "attribute 'bar' type is invalid"
    with pytest.raises(TypeError, match=err):

        class Foo(ExternalResource):
            bar: List[str]

            def __init__(self):
                ...


def test_external_attrtypes():
    class Foo(ExternalResource):
        a1: int
        a2: float
        a3: str

        def __init__(self):
            ...


def test_external_paramvalue_check(mocker):
    node = mocker.sentinel.NODE

    class Foo(ExternalResource):
        def __init__(self, *, bar: int):
            ...

    err = "argument 'bar' is not a number"
    with pytest.raises(TypeError, match=err):
        Foo(_ig_node=node, bar=String())

    err = "missing 1 required keyword-only argument: 'bar'"
    with pytest.raises(TypeError, match=err):
        Foo(_ig_node=node)


def test_external_paramvalue(mocker):
    from typing import List

    node = mocker.sentinel.NODE

    class Foo(ExternalResource):
        def __init__(
            self,
            *,
            p1: int,
            p1d: int = Number(42),
            p2: float,
            p2d: float = Number(42.42),
            p3: str,
            p3d: str = String("foo"),
            p4: List[int],
            p4d: List[int] = LISTS[Number]([Number(42)]),
            p5: List[float],
            p5d: List[float] = LISTS[Number]([Number(42.42)]),
            p6: List[str],
            p6d: List[str] = LISTS[String]([String("foo")]),
        ):
            assert not isinstance(p1, Static)
            assert not isinstance(p1d, Static)
            assert not isinstance(p2, Static)
            assert not isinstance(p2d, Static)
            assert not isinstance(p3, Static)
            assert not isinstance(p3d, Static)
            assert not isinstance(p4, Static)
            assert not isinstance(p4[Number(0)], SELECTS[Number])
            assert not isinstance(p4[Number(0)], Static)
            assert not isinstance(p4d, Static)
            assert not isinstance(p4d[Number(0)], SELECTS[Number])
            assert not isinstance(p4d[Number(0)], Static)
            assert not isinstance(p5, Static)
            assert not isinstance(p5d, Static)
            assert not isinstance(p6, Static)
            assert not isinstance(p6d, Static)

    Foo(
        _ig_node=node,
        p1=Number(42),
        p2=Number(42.42),
        p3=String("foo"),
        p4=LISTS[Number]([Number(42)]),
        p5=LISTS[Number]([Number(42.42)]),
        p6=LISTS[String]([String("foo")]),
    )


def test_external_attrinit(mocker):
    node = mocker.sentinel.NODE

    class Foo(ExternalResource):
        bar: int

        def __init__(self):
            ...

    err = "attribute 'bar' not initialized"
    with pytest.raises(AttributeError, match=err):
        Foo(_ig_node=node)


def test_external_noattr(mocker):
    node = mocker.sentinel.NODE

    class Foo(ExternalResource):
        def __init__(self):
            self.bar = Number()

    err = "attribute 'bar' doesn't exist"
    with pytest.raises(AttributeError, match=err):
        Foo(_ig_node=node)


def test_external_immutattr(mocker):
    node = mocker.sentinel.NODE

    class Foo(ExternalResource):
        bar: int

        def __init__(self):
            self.bar = Number()

    err = "attribute 'bar' is read-only"
    with pytest.raises(AttributeError, match=err):
        foo = Foo(_ig_node=node)
        foo.bar = Number()


def test_external_attrvalue_check(mocker):
    node = mocker.sentinel.NODE

    class Foo(ExternalResource):
        bar: int

        def __init__(self):
            self.bar = String()

    err = "value is not a number"
    with pytest.raises(TypeError, match=err):
        Foo(_ig_node=node)


def test_external_attrvalue(mocker):
    node = mocker.sentinel.NODE

    class Foo(ExternalResource):
        bar: str

        def __init__(self):
            self.bar = String("foo")

    assert not isinstance(Foo(_ig_node=node).bar, Static)


def test_getparmeters():
    from typing import List

    defaults = dict(
        p1d=Number(42),
        p2d=Number(42.42),
        p3d=String("foo"),
        p4d=LISTS[Number]([Number(42)]),
        p5d=LISTS[Number]([Number(42.42)]),
        p6d=LISTS[String]([String("foo")]),
    )

    class Foo(ExternalResource):
        def __init__(
            self,
            *,
            p1: int,
            p1d: int = defaults["p1d"],
            p2: float,
            p2d: float = defaults["p2d"],
            p3: str,
            p3d: str = defaults["p3d"],
            p4: List[int],
            p4d: List[int] = defaults["p4d"],
            p5: List[float],
            p5d: List[float] = defaults["p5d"],
            p6: List[str],
            p6d: List[str] = defaults["p6d"],
        ):
            ...

    params = _getparmeters(Foo)
    for k, v in params.items():
        d = f"{k}d" if not k.endswith("d") else k
        typ = type(defaults[d])
        assert isinstance(v, PARAMETERS[typ])
        assert isinstance(v, typ)
        assert not isinstance(v, Static)
        assert v._ig_name == k
        assert v._ig_default == defaults.get(k, None)


def test_asset_check():
    err = "asset name is not a static string"
    with pytest.raises(TypeError, match=err):
        Asset(name=String())

    err = "asset compress is not a static boolean"
    with pytest.raises(TypeError, match=err):
        Asset(name=String("foo"), compress=Boolean())

    err = "asset name includes path parts"
    with pytest.raises(ValueError, match=err):
        Asset(name=String("../foo"))

    err = "cannot retrieve text content from compressed asset"
    with pytest.raises(TypeError, match=err):
        Asset(name=String("__init__.py"), compress=Boolean(True)).text
