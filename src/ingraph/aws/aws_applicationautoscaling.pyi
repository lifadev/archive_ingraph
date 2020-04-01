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

_NAMESPACE = "AWS::ApplicationAutoScaling"

class ScalableTarget:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalabletarget.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        MaxCapacity: int,
        MinCapacity: int,
        ResourceId: str,
        RoleARN: str,
        ScalableDimension: str,
        ServiceNamespace: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ScheduledActions: List["ScalableTarget.ScheduledAction"] = ...,
        SuspendedState: "ScalableTarget.SuspendedState" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ScalableTargetAction:
        def __init__(self, *, MaxCapacity: int = ..., MinCapacity: int = ...): ...
    class ScheduledAction:
        def __init__(
            self,
            *,
            Schedule: str,
            ScheduledActionName: str,
            EndTime: str = ...,
            ScalableTargetAction: "ScalableTarget.ScalableTargetAction" = ...,
            StartTime: str = ...
        ): ...
    class SuspendedState:
        def __init__(
            self,
            *,
            DynamicScalingInSuspended: bool = ...,
            DynamicScalingOutSuspended: bool = ...,
            ScheduledScalingSuspended: bool = ...
        ): ...

class ScalingPolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PolicyName: str,
        PolicyType: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ResourceId: str = ...,
        ScalableDimension: str = ...,
        ScalingTargetId: str = ...,
        ServiceNamespace: str = ...,
        StepScalingPolicyConfiguration: "ScalingPolicy.StepScalingPolicyConfiguration" = ...,
        TargetTrackingScalingPolicyConfiguration: "ScalingPolicy.TargetTrackingScalingPolicyConfiguration" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CustomizedMetricSpecification:
        def __init__(
            self,
            *,
            MetricName: str,
            Namespace: str,
            Statistic: str,
            Dimensions: List["ScalingPolicy.MetricDimension"] = ...,
            Unit: str = ...
        ): ...
    class MetricDimension:
        def __init__(self, *, Name: str, Value: str): ...
    class PredefinedMetricSpecification:
        def __init__(self, *, PredefinedMetricType: str, ResourceLabel: str = ...): ...
    class StepAdjustment:
        def __init__(
            self,
            *,
            ScalingAdjustment: int,
            MetricIntervalLowerBound: float = ...,
            MetricIntervalUpperBound: float = ...
        ): ...
    class StepScalingPolicyConfiguration:
        def __init__(
            self,
            *,
            AdjustmentType: str = ...,
            Cooldown: int = ...,
            MetricAggregationType: str = ...,
            MinAdjustmentMagnitude: int = ...,
            StepAdjustments: List["ScalingPolicy.StepAdjustment"] = ...
        ): ...
    class TargetTrackingScalingPolicyConfiguration:
        def __init__(
            self,
            *,
            TargetValue: float,
            CustomizedMetricSpecification: "ScalingPolicy.CustomizedMetricSpecification" = ...,
            DisableScaleIn: bool = ...,
            PredefinedMetricSpecification: "ScalingPolicy.PredefinedMetricSpecification" = ...,
            ScaleInCooldown: int = ...,
            ScaleOutCooldown: int = ...
        ): ...
