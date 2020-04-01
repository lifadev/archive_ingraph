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

_NAMESPACE = "AWS::PinpointEmail"

class ConfigurationSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DeliveryOptions: "ConfigurationSet.DeliveryOptions" = ...,
        DependsOn: List[Any] = ...,
        ReputationOptions: "ConfigurationSet.ReputationOptions" = ...,
        SendingOptions: "ConfigurationSet.SendingOptions" = ...,
        Tags: List["ConfigurationSet.Tags"] = ...,
        TrackingOptions: "ConfigurationSet.TrackingOptions" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DeliveryOptions:
        def __init__(self, *, SendingPoolName: str = ...): ...
    class ReputationOptions:
        def __init__(self, *, ReputationMetricsEnabled: bool = ...): ...
    class SendingOptions:
        def __init__(self, *, SendingEnabled: bool = ...): ...
    class Tags:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...
    class TrackingOptions:
        def __init__(self, *, CustomRedirectDomain: str = ...): ...

class ConfigurationSetEventDestination:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-configurationseteventdestination.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ConfigurationSetName: str,
        EventDestinationName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EventDestination: "ConfigurationSetEventDestination.EventDestination" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CloudWatchDestination:
        def __init__(
            self,
            *,
            DimensionConfigurations: List[
                "ConfigurationSetEventDestination.DimensionConfiguration"
            ] = ...
        ): ...
    class DimensionConfiguration:
        def __init__(
            self,
            *,
            DefaultDimensionValue: str,
            DimensionName: str,
            DimensionValueSource: str
        ): ...
    class EventDestination:
        def __init__(
            self,
            *,
            MatchingEventTypes: List[str],
            CloudWatchDestination: "ConfigurationSetEventDestination.CloudWatchDestination" = ...,
            Enabled: bool = ...,
            KinesisFirehoseDestination: "ConfigurationSetEventDestination.KinesisFirehoseDestination" = ...,
            PinpointDestination: "ConfigurationSetEventDestination.PinpointDestination" = ...,
            SnsDestination: "ConfigurationSetEventDestination.SnsDestination" = ...
        ): ...
    class KinesisFirehoseDestination:
        def __init__(self, *, DeliveryStreamArn: str, IamRoleArn: str): ...
    class PinpointDestination:
        def __init__(self, *, ApplicationArn: str = ...): ...
    class SnsDestination:
        def __init__(self, *, TopicArn: str): ...

class DedicatedIpPool:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-dedicatedippool.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        PoolName: str = ...,
        Tags: List["DedicatedIpPool.Tags"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Tags:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...

class Identity:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpointemail-identity.html"""

    IdentityDNSRecordName3: Final[str]

    IdentityDNSRecordName1: Final[str]

    IdentityDNSRecordName2: Final[str]

    IdentityDNSRecordValue3: Final[str]

    IdentityDNSRecordValue2: Final[str]

    IdentityDNSRecordValue1: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DkimSigningEnabled: bool = ...,
        FeedbackForwardingEnabled: bool = ...,
        MailFromAttributes: "Identity.MailFromAttributes" = ...,
        Tags: List["Identity.Tags"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class MailFromAttributes:
        def __init__(
            self, *, BehaviorOnMxFailure: str = ..., MailFromDomain: str = ...
        ): ...
    class Tags:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...
