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

_NAMESPACE = "AWS::IoT1Click"

class Device:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-device.html"""

    DeviceId: Final[str]

    Enabled: Final[bool]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeviceId: str,
        Enabled: bool,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Placement:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-placement.html"""

    PlacementName: Final[str]

    ProjectName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ProjectName: str,
        AssociatedDevices: Any = ...,
        Attributes: Any = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        PlacementName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Project:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot1click-project.html"""

    ProjectName: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        PlacementTemplate: "Project.PlacementTemplate",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        ProjectName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DeviceTemplate:
        def __init__(self, *, CallbackOverrides: Any = ..., DeviceType: str = ...): ...
    class PlacementTemplate:
        def __init__(
            self, *, DefaultAttributes: Any = ..., DeviceTemplates: Any = ...
        ): ...
