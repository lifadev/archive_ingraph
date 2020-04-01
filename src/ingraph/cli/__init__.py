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

import importlib
import importlib.metadata
import importlib.resources
import json
import platform
import re
import sys
from typing import Any

import click

VER = importlib.metadata.version("ingraph")


@click.group(
    "ig",
    context_settings=dict(help_option_names=["-h", "--help"]),
    help=f"""\b
     ___        ____                 _
    |_ _|_ __  / ___|_ __ __ _ _ __ | |__
     | || '_ \| |  _| '__/ _` | '_ \| '_ \\
     | || | | | |_| | | | (_| | |_) | | | |
    |___|_| |_|\____|_|  \__,_| .__/|_| |_|
    https://lifa.dev/ingraph  |_|    v{VER}
    \b
    Infrastructure Graph DSL for AWS CloudFormation.
""",
)
@click.version_option(
    None,
    "-v",
    "--version",
    message=json.dumps(
        {
            "ingraph": VER,
            "python": platform.python_version(),
            platform.system().lower(): platform.release(),
            **{
                d: importlib.metadata.version(d)
                for d in [
                    re.split(r"[^a-zA-Z0-9_.-]", d)[0]
                    for d in (importlib.metadata.requires("ingraph") or [])
                ]
            },
        },
        indent=2,
    ),
)
def command() -> None:
    ...


def main() -> int:
    try:
        init()
        command.main(prog_name=command.name, args=sys.argv[1:], standalone_mode=False)
        return 0
    except click.ClickException as exc:
        exc.show()
        return exc.exit_code
    return 1  # type: ignore


def init() -> None:
    for name in importlib.resources.contents(__package__):
        if name.startswith("cmd_"):
            name = name[:-3] if name.endswith(".py") else name
            mod: Any = importlib.import_module(f".{name}", __package__)
            if hasattr(mod, "init"):
                mod.init()
            command.add_command(mod.command)
