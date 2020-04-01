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

from pathlib import Path

import pytest

from ingraph.engine import core
from ingraph.engine.importer import (aws_hook, external_hook, import_file,
                                     import_module)


@pytest.mark.parametrize(
    "lid,typ",
    [
        pytest.param(*t, id=t[0])
        for t in [
            ("account_id", core.AccountID),
            ("availability_zones", core.AvailabilityZones),
            ("notification_arns", core.NotificationARNs),
            ("partition", core.Partition),
            ("region", core.Region),
            ("stack_id", core.StackID),
            ("stack_name", core.StackName),
            ("url_suffix", core.URLSuffix),
        ]
    ],
)
def test_aws_pseudo(lid, typ):
    with aws_hook():
        from ingraph import aws

        val = getattr(aws, lid.upper())
        assert isinstance(val, typ)


@pytest.mark.parametrize(
    "lid,typ",
    [
        pytest.param(*t, id=t[0])
        for t in [("b64encode", core.Base64Encoded), ("cidr", core.CIDR),]
    ],
)
def test_aws_intrinsic(lid, typ):
    with aws_hook():
        from ingraph import aws

        val = getattr(aws, lid)
        assert issubclass(val, typ)


def test_aws_tag():
    with aws_hook():
        from ingraph import aws

        tag = aws.Tag(Key="key", Value="value")
        assert isinstance(tag, core.Property)


def test_aws_modules():
    base = Path(__file__).parent.parent.parent.parent / "src" / "ingraph" / "aws"
    with aws_hook():
        for file in list(base.glob("[a-z]*_*.pyi")):
            import_module(f"ingraph.aws.{file.stem}")


@pytest.mark.parametrize(
    "module,error",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            ("not_managed", "ingraph.engine", "No module named 'ingraph.engine'",),
            ("not_managed", "sys", "No module named 'sys'",),
            (
                "aws_notexists",
                "ingraph.aws.aws_exp",
                "No module named 'ingraph.aws.aws_exp'",
            ),
            ("module_notexists", "dummy", "No module named 'dummy'",),
        ]
    ],
)
def test_import_module(module, error):
    with pytest.raises(Exception, match=error):
        with external_hook():
            with aws_hook():
                import_module(module)


@pytest.mark.parametrize(
    "stmt,error",
    [
        pytest.param(*t[1:], id=t[0])
        for t in [
            ("not_managed", "from ingraph import cli", "Unexpected import",),
            ("not_managed", "from math import cos", "No module named 'math'"),
        ]
    ],
)
def test_import_file(stmt, error, tmpdir):
    path = tmpdir / "foo.py"
    path.write_text(stmt, "utf-8")
    with pytest.raises(Exception, match=error):
        with external_hook():
            with aws_hook():
                import_file(path)
