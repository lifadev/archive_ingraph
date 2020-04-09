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

import time
import zipfile
from io import BytesIO
from pathlib import Path

import pytest
from ingraph.engine.core import gethash, package_zip


def test_package_zip(tmpdir):
    path = Path(tmpdir.mkdir("package"))
    (path / "foo.txt").write_text("foo")
    (path / "bar").mkdir()
    (path / "bar" / "baz.txt").write_text("baz")
    (path / ".qux").touch()

    pack_file = package_zip(path / "foo.txt")
    with zipfile.ZipFile(pack_file.name, "r") as zip_file:
        assert zipfile.Path(zip_file, "foo.txt").is_file()

    pack_dir = package_zip(path)
    h1 = gethash(Path(pack_dir.name))

    with zipfile.ZipFile(pack_dir.name, "r") as zip_file:
        assert zipfile.Path(zip_file, "foo.txt").is_file()
        assert zipfile.Path(zip_file, "bar/").is_dir()
        assert zipfile.Path(zip_file, "bar/baz.txt").is_file()
        assert not zipfile.Path(zip_file, ".qux").exists()

    time.sleep(1)
    (path / "foo.txt").touch()

    pack_dir = package_zip(path)
    h2 = gethash(Path(pack_dir.name))

    assert h1 == h2

    pack_dir = package_zip(path, [path / "bar" / "baz.txt"])
    with zipfile.ZipFile(pack_dir.name, "r") as zip_file:
        assert not zipfile.Path(zip_file, str(path / "foo.txt")).exists()
        assert zipfile.Path(zip_file, str(path / "bar" / "baz.txt")).is_file()


def test_gethash_blob():
    h = gethash(BytesIO(b"foo"))

    assert h == "0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33"
