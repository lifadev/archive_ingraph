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

_NAMESPACE = "AWS::FMS"

class NotificationChannel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        SnsRoleName: str,
        SnsTopicArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Policy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-policy.html"""

    Id: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ExcludeResourceTags: bool,
        PolicyName: str,
        RemediationEnabled: bool,
        ResourceType: str,
        SecurityServicePolicyData: Any,
        DeleteAllPolicyResources: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ExcludeMap: "Policy.IEMap" = ...,
        IncludeMap: "Policy.IEMap" = ...,
        ResourceTags: List["Policy.ResourceTag"] = ...,
        ResourceTypeList: List[str] = ...,
        Tags: List["Policy.PolicyTag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class IEMap:
        def __init__(self, *, ACCOUNT: List[str] = ...): ...
    class PolicyTag:
        def __init__(self, *, Key: str, Value: str): ...
    class ResourceTag:
        def __init__(self, *, Key: str, Value: str = ...): ...
