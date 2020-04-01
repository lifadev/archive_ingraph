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

_NAMESPACE = "AWS::ElasticBeanstalk"

class Application:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        ResourceLifecycleConfig: "Application.ApplicationResourceLifecycleConfig" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ApplicationResourceLifecycleConfig:
        def __init__(
            self,
            *,
            ServiceRole: str = ...,
            VersionLifecycleConfig: "Application.ApplicationVersionLifecycleConfig" = ...
        ): ...
    class ApplicationVersionLifecycleConfig:
        def __init__(
            self,
            *,
            MaxAgeRule: "Application.MaxAgeRule" = ...,
            MaxCountRule: "Application.MaxCountRule" = ...
        ): ...
    class MaxAgeRule:
        def __init__(
            self,
            *,
            DeleteSourceFromS3: bool = ...,
            Enabled: bool = ...,
            MaxAgeInDays: int = ...
        ): ...
    class MaxCountRule:
        def __init__(
            self,
            *,
            DeleteSourceFromS3: bool = ...,
            Enabled: bool = ...,
            MaxCount: int = ...
        ): ...

class ApplicationVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-version.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationName: str,
        SourceBundle: "ApplicationVersion.SourceBundle",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class SourceBundle:
        def __init__(self, *, S3Bucket: str, S3Key: str): ...

class ConfigurationTemplate:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-configurationtemplate.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        EnvironmentId: str = ...,
        OptionSettings: List["ConfigurationTemplate.ConfigurationOptionSetting"] = ...,
        PlatformArn: str = ...,
        SolutionStackName: str = ...,
        SourceConfiguration: "ConfigurationTemplate.SourceConfiguration" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ConfigurationOptionSetting:
        def __init__(
            self,
            *,
            Namespace: str,
            OptionName: str,
            ResourceName: str = ...,
            Value: str = ...
        ): ...
    class SourceConfiguration:
        def __init__(self, *, ApplicationName: str, TemplateName: str): ...

class Environment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-beanstalk-environment.html"""

    EndpointURL: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationName: str,
        CNAMEPrefix: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        EnvironmentName: str = ...,
        OptionSettings: List["Environment.OptionSetting"] = ...,
        PlatformArn: str = ...,
        SolutionStackName: str = ...,
        Tags: List["Tag"] = ...,
        TemplateName: str = ...,
        Tier: "Environment.Tier" = ...,
        UpdateReplacePolicy: str = ...,
        VersionLabel: str = ...
    ): ...
    class OptionSetting:
        def __init__(
            self,
            *,
            Namespace: str,
            OptionName: str,
            ResourceName: str = ...,
            Value: str = ...
        ): ...
    class Tier:
        def __init__(self, *, Name: str = ..., Type: str = ..., Version: str = ...): ...
