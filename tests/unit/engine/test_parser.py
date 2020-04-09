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
import types

import pytest
from ingraph.engine import core, importer, parser
from ingraph.engine.parser import (CallWrapper, DefinitionWrapper,
                                   FStringWrapper, ImmutabilityGuard,
                                   LocationEnricher, PrivateChecker,
                                   SignatureModifier, TypeWrapper, process)


@pytest.mark.parametrize(
    "source",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            (
                "import",
                """
                from foo import _bar
                """,
            ),
            (
                "import",
                """
                from foo import bar as _baz
                """,
            ),
            (
                "class",
                """
                class _Foo:
                    def __init__(self):
                        ...
                """,
            ),
            (
                "param",
                """
                class Foo:
                    def __init__(self, _foo):
                        ...
                """,
            ),
            (
                "var",
                """
                class Foo:
                    def __init__(self):
                        _foo = 42
                """,
            ),
            (
                "attr",
                """
                class Foo:
                    def __init__(self):
                        foo._bar = 42
                """,
            ),
            (
                "call",
                """
                class Foo:
                    def __init__(self):
                        _foo()
                """,
            ),
            (
                "arg",
                """
                class Foo:
                    def __init__(self):
                        foo(_bar=42)
                """,
            ),
        ]
    ],
)
def test_private_names(source, mocker):
    module = types.ModuleType("<adhoc>")
    mocker.patch.object(parser, "TRANSFORMERS", [PrivateChecker])

    err = "names cannot start with an underscore"
    with pytest.raises(SyntaxError, match=err):
        process(textwrap.dedent(source), "<test>", module)


def test_signature_modifier(mocker):
    source = textwrap.dedent(
        """
        class Foo:
            def __init__(self, foo, bar=42):
                ...
        """
    )
    module = types.ModuleType("<adhoc>")
    mocker.patch.object(parser, "TRANSFORMERS", [SignatureModifier])
    process(source, "<test>", module)
    sig = inspect.signature(module.Foo)
    params = sig.parameters

    assert all(p.kind == inspect.Parameter.KEYWORD_ONLY for p in params.values())
    assert params["foo"].default == inspect.Parameter.empty
    assert params["bar"].default == 42


def test_immutability(mocker):
    source = textwrap.dedent(
        """
        class Foo:
            def __init__(self):
                self.baz = 42
                self.baz = 24
                bar = 42
                bar = 24
        """
    )
    module = types.ModuleType("<adhoc>")
    mocker.patch.object(parser, "TRANSFORMERS", [ImmutabilityGuard])
    process(source, "<test>", module)

    with pytest.raises(TypeError, match="'bar' is read-only"):
        module.Foo()


def test_definition_wrapper(mocker):
    source = textwrap.dedent(
        """
        class Foo:
            def __init__(self):
                ...
        """
    )
    module = types.ModuleType("<adhoc>")
    mocker.patch.object(parser, "TRANSFORMERS", [DefinitionWrapper])
    process(source, "<test>", module)

    assert issubclass(module.Foo, core.ExternalResource)


def test_definition_wrapper_custom(mocker):
    source = textwrap.dedent(
        """
        class Foo(CustomResource):
            Bar: int
        """
    )
    module = types.ModuleType("<adhoc>")
    mocker.patch.object(parser, "TRANSFORMERS", [DefinitionWrapper])
    with importer.aws_hook():
        from ingraph.aws.aws_cloudformation import CustomResource

        module.CustomResource = CustomResource
        process(source, "<test>", module)

        assert issubclass(module.Foo, core.CustomResource)
        assert issubclass(module.Foo, CustomResource)


def test_type_wrapper(mocker):
    source = textwrap.dedent(
        """
        class Foo:
            def __init__(self, p = 42) -> None:
                ...
                self.p = p
                self.b = True
                self.n = 42
                self.s = "foo"
                self.m = {
                    "b": True,
                    "n": 42,
                    "s": "foo",
                    "m": {}
                }
                self.lb = [True, False]
                self.ln = [4.2, -42]
                self.ls = ["foo", "bar"]
                self.lf = [True, [4, "foo"], {"s": "bar"}]
        """
    )
    module = types.ModuleType("<adhoc>")
    mocker.patch.object(parser, "TRANSFORMERS", [TypeWrapper])
    process(source, "<test>", module)
    foo = module.Foo()

    assert isinstance(foo.p, core.Number)
    assert isinstance(foo.b, core.Boolean)
    assert isinstance(foo.n, core.Number)
    assert isinstance(foo.s, core.String)
    assert isinstance(foo.m, core.Map)
    assert all(isinstance(k, core.String) for k in foo.m._ig_value)
    mkvs = [type(v) for v in foo.m._ig_value.values()]
    assert mkvs == [core.Boolean, core.Number, core.String, core.Map]
    assert isinstance(foo.lb, core.LISTS[core.Boolean])
    assert isinstance(foo.ln, core.LISTS[core.Number])
    assert isinstance(foo.ls, core.LISTS[core.String])
    assert isinstance(foo.lf, core.FreeList)


def test_type_wrapper_invalid(mocker):
    source = textwrap.dedent(
        """
        class Foo:
            def __init__(self):
                b""
        """
    )
    module = types.ModuleType("<adhoc>")
    mocker.patch.object(parser, "TRANSFORMERS", [TypeWrapper])

    err = "unsupported primitive type 'bytes'"
    with pytest.raises(SyntaxError, match=err):
        process(source, "<test>", module)


def test_location_enricher(mocker):
    source = textwrap.dedent(
        """

        class Foo:
            def __init__(self):
                ...
        """
    )
    module = types.ModuleType("<adhoc>")
    mocker.patch.object(parser, "TRANSFORMERS", [LocationEnricher])
    process(source, "<test>", module)

    assert module.Foo._ig_filename == "<test>"
    assert module.Foo._ig_lines == (3, 5)
    assert module.Foo._ig_columns == (0, 11)
    assert (
        module.Foo._ig_source
        == textwrap.dedent(
            """
            class Foo:
                def __init__(self):
                    ...
            """
        ).strip()
    )


def test_call_wrapper_python(mocker):
    for typ in {int, float, str}:
        source = textwrap.dedent(
            f"""
            class Foo:
                def __init__(self):
                    {typ.__name__}()
            """
        )
        module = types.ModuleType("<adhoc>")
        mocker.patch.object(parser, "TRANSFORMERS", [CallWrapper])
        process(source, "<test>", module)

        with pytest.raises(TypeError, match="invalid call"):
            module.Foo()


def test_call_wrapper_name_check(mocker):
    source = textwrap.dedent(
        """
        class Foo:
            def __init__(self):
                Bar()

        class Bar:
            def __init__(self):
                ...
        """
    )
    module = types.ModuleType("<adhoc>")
    mocker.patch.object(parser, "TRANSFORMERS", [DefinitionWrapper, CallWrapper])
    process(source, "<test>", module)

    node = mocker.sentinel.NODE
    err = "invalid resource instantiation"
    with pytest.raises(TypeError, match=err):
        module.Foo(_ig_node=node)


def test_call_wrapper_proxy(mocker):
    source = textwrap.dedent(
        """
        class Foo:
            def __init__(self):
                bar()
        """
    )
    module = types.ModuleType("<adhoc>")
    module.bar = mocker.stub()
    mocker.patch.object(parser, "TRANSFORMERS", [CallWrapper])
    process(source, "<test>", module)

    module.Foo()

    module.bar.assert_called_once()


def test_call_wrapper(mocker):
    source = textwrap.dedent(
        """
        class Foo:
            def __init__(self):
                bar = Bar()

        class Bar:
            def __init__(self):
                ...
        """
    )
    module = types.ModuleType("<adhoc>")
    mocker.patch.object(
        parser, "TRANSFORMERS", [DefinitionWrapper, LocationEnricher, CallWrapper]
    )
    process(source, "<test>", module)
    node = mocker.sentinel.NODE

    with core.new_graph(module.Foo) as graph:
        foo = module.Foo()

    lineages = [n.lineage for n in graph.nodes()]
    assert lineages == [core.ROOT, core.ROOT + ("bar",)]

    resources = [n.resource for n in graph.nodes()]
    assert isinstance(resources[0], module.Foo)
    assert isinstance(resources[1], module.Bar)


def test_fstring_wrapper(mocker):
    source = textwrap.dedent(
        """
        class Foo:
            def __init__(self):
                n = 42
                s = 'baz'
                self.bar = f"{n} {s}"
        """
    )
    module = types.ModuleType("<adhoc>")
    mocker.patch.object(parser, "TRANSFORMERS", [TypeWrapper, FStringWrapper])
    process(source, "<test>", module)
    bar = module.Foo().bar

    assert isinstance(bar, core.Sub)
    values = [v._ig_value for v in bar._ig_kwargs._ig_value.values()]
    assert values == [42, " ", "baz"]
