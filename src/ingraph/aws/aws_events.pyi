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

_NAMESPACE = "AWS::Events"

class EventBus:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbus.html"""

    Policy: Final[str]

    Arn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EventSourceName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class EventBusPolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-eventbuspolicy.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Action: str,
        Principal: str,
        StatementId: str,
        Condition: "EventBusPolicy.Condition" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EventBusName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Condition:
        def __init__(self, *, Key: str = ..., Type: str = ..., Value: str = ...): ...

class Rule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-rule.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        EventBusName: str = ...,
        EventPattern: Any = ...,
        Name: str = ...,
        RoleArn: str = ...,
        ScheduleExpression: str = ...,
        State: str = ...,
        Targets: List["Rule.Target"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AwsVpcConfiguration:
        def __init__(
            self,
            *,
            Subnets: List[str],
            AssignPublicIp: str = ...,
            SecurityGroups: List[str] = ...
        ): ...
    class BatchArrayProperties:
        def __init__(self, *, Size: int = ...): ...
    class BatchParameters:
        def __init__(
            self,
            *,
            JobDefinition: str,
            JobName: str,
            ArrayProperties: "Rule.BatchArrayProperties" = ...,
            RetryStrategy: "Rule.BatchRetryStrategy" = ...
        ): ...
    class BatchRetryStrategy:
        def __init__(self, *, Attempts: int = ...): ...
    class EcsParameters:
        def __init__(
            self,
            *,
            TaskDefinitionArn: str,
            Group: str = ...,
            LaunchType: str = ...,
            NetworkConfiguration: "Rule.NetworkConfiguration" = ...,
            PlatformVersion: str = ...,
            TaskCount: int = ...
        ): ...
    class InputTransformer:
        def __init__(
            self, *, InputTemplate: str, InputPathsMap: Dict[str, str] = ...
        ): ...
    class KinesisParameters:
        def __init__(self, *, PartitionKeyPath: str): ...
    class NetworkConfiguration:
        def __init__(
            self, *, AwsVpcConfiguration: "Rule.AwsVpcConfiguration" = ...
        ): ...
    class RunCommandParameters:
        def __init__(self, *, RunCommandTargets: List["Rule.RunCommandTarget"]): ...
    class RunCommandTarget:
        def __init__(self, *, Key: str, Values: List[str]): ...
    class SqsParameters:
        def __init__(self, *, MessageGroupId: str): ...
    class Target:
        def __init__(
            self,
            *,
            Arn: str,
            Id: str,
            BatchParameters: "Rule.BatchParameters" = ...,
            EcsParameters: "Rule.EcsParameters" = ...,
            Input: str = ...,
            InputPath: str = ...,
            InputTransformer: "Rule.InputTransformer" = ...,
            KinesisParameters: "Rule.KinesisParameters" = ...,
            RoleArn: str = ...,
            RunCommandParameters: "Rule.RunCommandParameters" = ...,
            SqsParameters: "Rule.SqsParameters" = ...
        ): ...
