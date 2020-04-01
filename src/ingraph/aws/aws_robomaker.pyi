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

_NAMESPACE = "AWS::RoboMaker"

class Fleet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-fleet.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Robot:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robot.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Architecture: str,
        GreengrassGroupId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Fleet: str = ...,
        Name: str = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class RobotApplication:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplication.html"""

    CurrentRevisionId: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        RobotSoftwareSuite: "RobotApplication.RobotSoftwareSuite",
        Sources: List["RobotApplication.SourceConfig"],
        CurrentRevisionId: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class RobotSoftwareSuite:
        def __init__(self, *, Name: str, Version: str): ...
    class SourceConfig:
        def __init__(self, *, Architecture: str, S3Bucket: str, S3Key: str): ...

class RobotApplicationVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-robotapplicationversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Application: str,
        CurrentRevisionId: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class SimulationApplication:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplication.html"""

    CurrentRevisionId: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        RenderingEngine: "SimulationApplication.RenderingEngine",
        RobotSoftwareSuite: "SimulationApplication.RobotSoftwareSuite",
        SimulationSoftwareSuite: "SimulationApplication.SimulationSoftwareSuite",
        Sources: List["SimulationApplication.SourceConfig"],
        CurrentRevisionId: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class RenderingEngine:
        def __init__(self, *, Name: str, Version: str): ...
    class RobotSoftwareSuite:
        def __init__(self, *, Name: str, Version: str): ...
    class SimulationSoftwareSuite:
        def __init__(self, *, Name: str, Version: str): ...
    class SourceConfig:
        def __init__(self, *, Architecture: str, S3Bucket: str, S3Key: str): ...

class SimulationApplicationVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-robomaker-simulationapplicationversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Application: str,
        CurrentRevisionId: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
