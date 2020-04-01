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

import importlib.resources
import logging
import os
import subprocess

import pytest

from . import fixture

LOGGER = logging.getLogger(__name__)

TESTS = [f for f in importlib.resources.contents(fixture) if not f.startswith("_")]


@pytest.mark.parametrize("tid", TESTS)
def test_file(tid, tmpdir):
    output = tmpdir / "output.yaml"
    with importlib.resources.path(fixture, tid) as path:
        if path.name == "complete_module":
            return
        res = subprocess.run(
            f"ig cfn -i input.py -r Entrypoint -o {str(output)}",
            cwd=path,
            capture_output=True,
            shell=True,
            encoding="utf-8",
        )
        if res.stderr:
            LOGGER.info("[stderr]\n%s", res.stderr)
        if res.stdout:
            LOGGER.info("[stdout]\n%s", res.stdout)
        if res.returncode:
            assert False, "unexpected command failure"
        want = (path / "output.yaml").read_text("utf-8")
        got = output.read_text("utf-8")
        assert got == want, str(output)


@pytest.mark.parametrize("tid", TESTS)
def test_module(tid, tmpdir):
    output = tmpdir / "output.yaml"
    with importlib.resources.path(fixture, tid) as path:
        if path.name == "complete_file":
            return
        env = {k: v for k, v in os.environ.items()}
        env.update(PYTHONPATH=".")
        res = subprocess.run(
            f"ig cfn -i {path.name}.input -r Entrypoint -o {str(output)}",
            cwd=path.parent,
            capture_output=True,
            shell=True,
            encoding="utf-8",
            env=env,
        )
        if res.stderr:
            LOGGER.info("[stderr]\n%s", res.stderr)
        if res.stdout:
            LOGGER.info("[stdout]\n%s", res.stdout)
        if res.returncode:
            assert False, "unexpected command failure"
        want = (path / "output.yaml").read_text("utf-8")
        got = output.read_text("utf-8")
        assert got == want, str(output)
        # print(str(output))
