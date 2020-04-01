# Copyright 2020 Farzad Senart and Lionel Suss. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Dict, Final, List

from . import Tag

_NAMESPACE = "AWS::IoTThingsGraph"

class FlowTemplate:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotthingsgraph-flowtemplate.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Definition: "FlowTemplate.DefinitionDocument",
        CompatibleNamespaceVersion: float = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DefinitionDocument:
        def __init__(self, *, Language: str, Text: str): ...
