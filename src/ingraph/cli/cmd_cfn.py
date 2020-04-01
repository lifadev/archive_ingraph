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
from shutil import copyfile

import click

from .. import engine


@click.command(name="cfn")
@click.option(
    "--input",
    "-i",
    "input_",
    metavar="FILE|MODULE",
    help="Read graph from file or module.",
    required=True,
)
@click.option(
    "--root", "-r", metavar="DEFINITION", help="Start with definition.", required=True,
)
@click.option(
    "--output", "-o", metavar="FILE", help="Write YAML to file.", required=True,
)
def command(input_: str, root: str, output: str) -> None:
    """Translate infrastructure graphs to CloudFormation templates."""

    template, assets = engine.tocfn(input_, root)
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    Path(output).write_text(template, "utf-8")
    for k, v in assets.items():
        copyfile(v, Path(output).parent / k)
