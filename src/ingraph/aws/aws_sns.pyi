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

_NAMESPACE = "AWS::SNS"

class Subscription:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Protocol: str,
        TopicArn: str,
        DeletionPolicy: str = ...,
        DeliveryPolicy: Any = ...,
        DependsOn: List[Any] = ...,
        Endpoint: str = ...,
        FilterPolicy: Any = ...,
        RawMessageDelivery: bool = ...,
        RedrivePolicy: Any = ...,
        Region: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Topic:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-topic.html"""

    TopicName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DisplayName: str = ...,
        KmsMasterKeyId: str = ...,
        Subscription: List["Topic.Subscription"] = ...,
        Tags: List["Tag"] = ...,
        TopicName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Subscription:
        def __init__(self, *, Endpoint: str, Protocol: str): ...

class TopicPolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PolicyDocument: Any,
        Topics: List[str],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
