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

_NAMESPACE = "AWS::Logs"

class Destination:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-destination.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DestinationName: str,
        DestinationPolicy: str,
        RoleArn: str,
        TargetArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class LogGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        LogGroupName: str = ...,
        RetentionInDays: int = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class LogStream:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-logstream.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        LogGroupName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        LogStreamName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class MetricFilter:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-metricfilter.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        FilterPattern: str,
        LogGroupName: str,
        MetricTransformations: List["MetricFilter.MetricTransformation"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class MetricTransformation:
        def __init__(
            self,
            *,
            MetricName: str,
            MetricNamespace: str,
            MetricValue: str,
            DefaultValue: float = ...
        ): ...

class SubscriptionFilter:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-subscriptionfilter.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DestinationArn: str,
        FilterPattern: str,
        LogGroupName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RoleArn: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
