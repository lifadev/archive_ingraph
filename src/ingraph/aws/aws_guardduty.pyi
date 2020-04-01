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

_NAMESPACE = "AWS::GuardDuty"

class Detector:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Enable: bool,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        FindingPublishingFrequency: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Filter:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-filter.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Action: str,
        Description: str,
        DetectorId: str,
        FindingCriteria: "Filter.FindingCriteria",
        Name: str,
        Rank: int,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Condition:
        def __init__(
            self,
            *,
            Eq: List[str] = ...,
            Gte: int = ...,
            Lt: int = ...,
            Lte: int = ...,
            Neq: List[str] = ...
        ): ...
    class FindingCriteria:
        def __init__(
            self, *, Criterion: Any = ..., ItemType: "Filter.Condition" = ...
        ): ...

class IPSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-ipset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Activate: bool,
        DetectorId: str,
        Format: str,
        Location: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Master:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-master.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DetectorId: str,
        MasterId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InvitationId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Member:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-member.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DetectorId: str,
        Email: str,
        MemberId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DisableEmailNotification: bool = ...,
        Message: str = ...,
        Status: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ThreatIntelSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-threatintelset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Activate: bool,
        DetectorId: str,
        Format: str,
        Location: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
