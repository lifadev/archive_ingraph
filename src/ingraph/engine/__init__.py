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
from typing import Mapping, Tuple

import networkx as nx
from ruamel.yaml import YAML

from . import core, encoder, importer


def tocfn(target: str, entrypoint: str) -> Tuple[str, Mapping[str, Path]]:
    with importer.external_hook():
        with importer.aws_hook():
            module = importer.import_target(target)
            root = getattr(module, entrypoint)
            graph = core.process(root)
            return encoder.encode_cfn(graph)
