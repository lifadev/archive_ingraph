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

_NAMESPACE = "AWS::IoTEvents"

class DetectorModel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-detectormodel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DetectorModelDefinition: "DetectorModel.DetectorModelDefinition" = ...,
        DetectorModelDescription: str = ...,
        DetectorModelName: str = ...,
        EvaluationMethod: str = ...,
        Key: str = ...,
        RoleArn: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Action:
        def __init__(
            self,
            *,
            ClearTimer: "DetectorModel.ClearTimer" = ...,
            Firehose: "DetectorModel.Firehose" = ...,
            IotEvents: "DetectorModel.IotEvents" = ...,
            IotTopicPublish: "DetectorModel.IotTopicPublish" = ...,
            Lambda: "DetectorModel.Lambda" = ...,
            ResetTimer: "DetectorModel.ResetTimer" = ...,
            SetTimer: "DetectorModel.SetTimer" = ...,
            SetVariable: "DetectorModel.SetVariable" = ...,
            Sns: "DetectorModel.Sns" = ...,
            Sqs: "DetectorModel.Sqs" = ...
        ): ...
    class ClearTimer:
        def __init__(self, *, TimerName: str = ...): ...
    class DetectorModelDefinition:
        def __init__(
            self,
            *,
            InitialStateName: str = ...,
            States: List["DetectorModel.State"] = ...
        ): ...
    class Event:
        def __init__(
            self,
            *,
            Actions: List["DetectorModel.Action"] = ...,
            Condition: str = ...,
            EventName: str = ...
        ): ...
    class Firehose:
        def __init__(self, *, DeliveryStreamName: str = ..., Separator: str = ...): ...
    class IotEvents:
        def __init__(self, *, InputName: str = ...): ...
    class IotTopicPublish:
        def __init__(self, *, MqttTopic: str = ...): ...
    class Lambda:
        def __init__(self, *, FunctionArn: str = ...): ...
    class OnEnter:
        def __init__(self, *, Events: List["DetectorModel.Event"] = ...): ...
    class OnExit:
        def __init__(self, *, Events: List["DetectorModel.Event"] = ...): ...
    class OnInput:
        def __init__(
            self,
            *,
            Events: List["DetectorModel.Event"] = ...,
            TransitionEvents: List["DetectorModel.TransitionEvent"] = ...
        ): ...
    class ResetTimer:
        def __init__(self, *, TimerName: str = ...): ...
    class SetTimer:
        def __init__(
            self,
            *,
            DurationExpression: str = ...,
            Seconds: int = ...,
            TimerName: str = ...
        ): ...
    class SetVariable:
        def __init__(self, *, Value: str = ..., VariableName: str = ...): ...
    class Sns:
        def __init__(self, *, TargetArn: str = ...): ...
    class Sqs:
        def __init__(self, *, QueueUrl: str = ..., UseBase64: bool = ...): ...
    class State:
        def __init__(
            self,
            *,
            OnEnter: "DetectorModel.OnEnter" = ...,
            OnExit: "DetectorModel.OnExit" = ...,
            OnInput: "DetectorModel.OnInput" = ...,
            StateName: str = ...
        ): ...
    class TransitionEvent:
        def __init__(
            self,
            *,
            Actions: List["DetectorModel.Action"] = ...,
            Condition: str = ...,
            EventName: str = ...,
            NextState: str = ...
        ): ...

class Input:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotevents-input.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InputDefinition: "Input.InputDefinition" = ...,
        InputDescription: str = ...,
        InputName: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Attribute:
        def __init__(self, *, JsonPath: str = ...): ...
    class InputDefinition:
        def __init__(self, *, Attributes: List["Input.Attribute"] = ...): ...
