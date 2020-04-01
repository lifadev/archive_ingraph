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

_NAMESPACE = "AWS::DLM"

class LifecyclePolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dlm-lifecyclepolicy.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        ExecutionRoleArn: str = ...,
        PolicyDetails: "LifecyclePolicy.PolicyDetails" = ...,
        State: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CreateRule:
        def __init__(
            self, *, Interval: int, IntervalUnit: str, Times: List[str] = ...
        ): ...
    class CrossRegionCopyRetainRule:
        def __init__(self, *, Interval: int = ..., IntervalUnit: str = ...): ...
    class CrossRegionCopyRule:
        def __init__(
            self,
            *,
            CmkArn: str = ...,
            CopyTags: bool = ...,
            Encrypted: bool = ...,
            RetainRule: "LifecyclePolicy.CrossRegionCopyRetainRule" = ...,
            TargetRegion: str = ...
        ): ...
    class FastRestoreRule:
        def __init__(
            self,
            *,
            AvailabilityZones: List[str] = ...,
            Count: int = ...,
            Interval: int = ...,
            IntervalUnit: str = ...
        ): ...
    class Parameters:
        def __init__(self, *, ExcludeBootVolume: bool = ...): ...
    class PolicyDetails:
        def __init__(
            self,
            *,
            ResourceTypes: List[str],
            Schedules: List["LifecyclePolicy.Schedule"],
            TargetTags: List["Tag"],
            Parameters: "LifecyclePolicy.Parameters" = ...,
            PolicyType: str = ...
        ): ...
    class RetainRule:
        def __init__(
            self, *, Count: int = ..., Interval: int = ..., IntervalUnit: str = ...
        ): ...
    class Schedule:
        def __init__(
            self,
            *,
            CopyTags: bool = ...,
            CreateRule: "LifecyclePolicy.CreateRule" = ...,
            CrossRegionCopyRules: List["LifecyclePolicy.CrossRegionCopyRule"] = ...,
            FastRestoreRule: "LifecyclePolicy.FastRestoreRule" = ...,
            Name: str = ...,
            RetainRule: "LifecyclePolicy.RetainRule" = ...,
            TagsToAdd: List["Tag"] = ...,
            VariableTags: List["Tag"] = ...
        ): ...
