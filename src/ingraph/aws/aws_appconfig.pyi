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

_NAMESPACE = "AWS::AppConfig"

class Application:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-application.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Tags: List["Application.Tags"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Tags:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...

class ConfigurationProfile:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-configurationprofile.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        LocationUri: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        RetrievalRoleArn: str = ...,
        Tags: List["ConfigurationProfile.Tags"] = ...,
        UpdateReplacePolicy: str = ...,
        Validators: List["ConfigurationProfile.Validators"] = ...
    ): ...
    class Tags:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...
    class Validators:
        def __init__(self, *, Content: str = ..., Type: str = ...): ...

class Deployment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        ConfigurationProfileId: str,
        ConfigurationVersion: str,
        DeploymentStrategyId: str,
        EnvironmentId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Tags: List["Deployment.Tags"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Tags:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...

class DeploymentStrategy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deploymentstrategy.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeploymentDurationInMinutes: float,
        GrowthFactor: float,
        Name: str,
        ReplicateTo: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        FinalBakeTimeInMinutes: float = ...,
        GrowthType: str = ...,
        Tags: List["DeploymentStrategy.Tags"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Tags:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...

class Environment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-environment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Monitors: List["Environment.Monitors"] = ...,
        Tags: List["Environment.Tags"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Monitors:
        def __init__(self, *, AlarmArn: str = ..., AlarmRoleArn: str = ...): ...
    class Tags:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...
