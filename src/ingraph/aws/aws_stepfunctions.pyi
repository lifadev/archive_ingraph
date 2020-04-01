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

_NAMESPACE = "AWS::StepFunctions"

class Activity:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-activity.html"""

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Activity.TagsEntry"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class TagsEntry:
        def __init__(self, *, Key: str, Value: str): ...

class StateMachine:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html"""

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DefinitionString: str,
        RoleArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        LoggingConfiguration: "StateMachine.LoggingConfiguration" = ...,
        StateMachineName: str = ...,
        StateMachineType: str = ...,
        Tags: List["StateMachine.TagsEntry"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CloudWatchLogsLogGroup:
        def __init__(self, *, LogGroupArn: str): ...
    class LogDestination:
        def __init__(
            self, *, CloudWatchLogsLogGroup: "StateMachine.CloudWatchLogsLogGroup" = ...
        ): ...
    class LoggingConfiguration:
        def __init__(
            self,
            *,
            Destinations: List["StateMachine.LogDestination"] = ...,
            IncludeExecutionData: bool = ...,
            Level: str = ...
        ): ...
    class TagsEntry:
        def __init__(self, *, Key: str, Value: str): ...
