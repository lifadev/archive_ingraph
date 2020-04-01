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

_NAMESPACE = "AWS::AutoScalingPlans"

class ScalingPlan:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-autoscalingplans-scalingplan.html"""

    ScalingPlanName: Final[str]

    ScalingPlanVersion: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationSource: "ScalingPlan.ApplicationSource",
        ScalingInstructions: List["ScalingPlan.ScalingInstruction"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ApplicationSource:
        def __init__(
            self,
            *,
            CloudFormationStackARN: str = ...,
            TagFilters: List["ScalingPlan.TagFilter"] = ...
        ): ...
    class CustomizedLoadMetricSpecification:
        def __init__(
            self,
            *,
            MetricName: str,
            Namespace: str,
            Statistic: str,
            Dimensions: List["ScalingPlan.MetricDimension"] = ...,
            Unit: str = ...
        ): ...
    class CustomizedScalingMetricSpecification:
        def __init__(
            self,
            *,
            MetricName: str,
            Namespace: str,
            Statistic: str,
            Dimensions: List["ScalingPlan.MetricDimension"] = ...,
            Unit: str = ...
        ): ...
    class MetricDimension:
        def __init__(self, *, Name: str, Value: str): ...
    class PredefinedLoadMetricSpecification:
        def __init__(
            self, *, PredefinedLoadMetricType: str, ResourceLabel: str = ...
        ): ...
    class PredefinedScalingMetricSpecification:
        def __init__(
            self, *, PredefinedScalingMetricType: str, ResourceLabel: str = ...
        ): ...
    class ScalingInstruction:
        def __init__(
            self,
            *,
            MaxCapacity: int,
            MinCapacity: int,
            ResourceId: str,
            ScalableDimension: str,
            ServiceNamespace: str,
            TargetTrackingConfigurations: List[
                "ScalingPlan.TargetTrackingConfiguration"
            ],
            CustomizedLoadMetricSpecification: "ScalingPlan.CustomizedLoadMetricSpecification" = ...,
            DisableDynamicScaling: bool = ...,
            PredefinedLoadMetricSpecification: "ScalingPlan.PredefinedLoadMetricSpecification" = ...,
            PredictiveScalingMaxCapacityBehavior: str = ...,
            PredictiveScalingMaxCapacityBuffer: int = ...,
            PredictiveScalingMode: str = ...,
            ScalingPolicyUpdateBehavior: str = ...,
            ScheduledActionBufferTime: int = ...
        ): ...
    class TagFilter:
        def __init__(self, *, Key: str, Values: List[str] = ...): ...
    class TargetTrackingConfiguration:
        def __init__(
            self,
            *,
            TargetValue: float,
            CustomizedScalingMetricSpecification: "ScalingPlan.CustomizedScalingMetricSpecification" = ...,
            DisableScaleIn: bool = ...,
            EstimatedInstanceWarmup: int = ...,
            PredefinedScalingMetricSpecification: "ScalingPlan.PredefinedScalingMetricSpecification" = ...,
            ScaleInCooldown: int = ...,
            ScaleOutCooldown: int = ...
        ): ...
