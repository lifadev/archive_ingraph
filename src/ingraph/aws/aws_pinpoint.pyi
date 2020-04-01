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

_NAMESPACE = "AWS::Pinpoint"

class ADMChannel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-admchannel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        ClientId: str,
        ClientSecret: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Enabled: bool = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class APNSChannel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnschannel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        BundleId: str = ...,
        Certificate: str = ...,
        DefaultAuthenticationMethod: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Enabled: bool = ...,
        PrivateKey: str = ...,
        TeamId: str = ...,
        TokenKey: str = ...,
        TokenKeyId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class APNSSandboxChannel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnssandboxchannel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        BundleId: str = ...,
        Certificate: str = ...,
        DefaultAuthenticationMethod: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Enabled: bool = ...,
        PrivateKey: str = ...,
        TeamId: str = ...,
        TokenKey: str = ...,
        TokenKeyId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class APNSVoipChannel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipchannel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        BundleId: str = ...,
        Certificate: str = ...,
        DefaultAuthenticationMethod: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Enabled: bool = ...,
        PrivateKey: str = ...,
        TeamId: str = ...,
        TokenKey: str = ...,
        TokenKeyId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class APNSVoipSandboxChannel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-apnsvoipsandboxchannel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        BundleId: str = ...,
        Certificate: str = ...,
        DefaultAuthenticationMethod: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Enabled: bool = ...,
        PrivateKey: str = ...,
        TeamId: str = ...,
        TokenKey: str = ...,
        TokenKeyId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class App:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-app.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ApplicationSettings:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-applicationsettings.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        CampaignHook: "ApplicationSettings.CampaignHook" = ...,
        CloudWatchMetricsEnabled: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Limits: "ApplicationSettings.Limits" = ...,
        QuietTime: "ApplicationSettings.QuietTime" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CampaignHook:
        def __init__(
            self, *, LambdaFunctionName: str = ..., Mode: str = ..., WebUrl: str = ...
        ): ...
    class Limits:
        def __init__(
            self,
            *,
            Daily: int = ...,
            MaximumDuration: int = ...,
            MessagesPerSecond: int = ...,
            Total: int = ...
        ): ...
    class QuietTime:
        def __init__(self, *, End: str, Start: str): ...

class BaiduChannel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-baiduchannel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiKey: str,
        ApplicationId: str,
        SecretKey: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Enabled: bool = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Campaign:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-campaign.html"""

    CampaignId: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        MessageConfiguration: "Campaign.MessageConfiguration",
        Name: str,
        Schedule: "Campaign.Schedule",
        SegmentId: str,
        AdditionalTreatments: List["Campaign.WriteTreatmentResource"] = ...,
        CampaignHook: "Campaign.CampaignHook" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        HoldoutPercent: int = ...,
        IsPaused: bool = ...,
        Limits: "Campaign.Limits" = ...,
        SegmentVersion: int = ...,
        Tags: Any = ...,
        TreatmentDescription: str = ...,
        TreatmentName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AttributeDimension:
        def __init__(self, *, AttributeType: str = ..., Values: List[str] = ...): ...
    class CampaignEmailMessage:
        def __init__(
            self,
            *,
            Body: str = ...,
            FromAddress: str = ...,
            HtmlBody: str = ...,
            Title: str = ...
        ): ...
    class CampaignEventFilter:
        def __init__(
            self, *, Dimensions: "Campaign.EventDimensions" = ..., FilterType: str = ...
        ): ...
    class CampaignHook:
        def __init__(
            self, *, LambdaFunctionName: str = ..., Mode: str = ..., WebUrl: str = ...
        ): ...
    class CampaignSmsMessage:
        def __init__(
            self, *, Body: str = ..., MessageType: str = ..., SenderId: str = ...
        ): ...
    class EventDimensions:
        def __init__(
            self,
            *,
            Attributes: Any = ...,
            EventType: "Campaign.SetDimension" = ...,
            Metrics: Any = ...
        ): ...
    class Limits:
        def __init__(
            self,
            *,
            Daily: int = ...,
            MaximumDuration: int = ...,
            MessagesPerSecond: int = ...,
            Total: int = ...
        ): ...
    class Message:
        def __init__(
            self,
            *,
            Action: str = ...,
            Body: str = ...,
            ImageIconUrl: str = ...,
            ImageSmallIconUrl: str = ...,
            ImageUrl: str = ...,
            JsonBody: str = ...,
            MediaUrl: str = ...,
            RawContent: str = ...,
            SilentPush: bool = ...,
            TimeToLive: int = ...,
            Title: str = ...,
            Url: str = ...
        ): ...
    class MessageConfiguration:
        def __init__(
            self,
            *,
            ADMMessage: "Campaign.Message" = ...,
            APNSMessage: "Campaign.Message" = ...,
            BaiduMessage: "Campaign.Message" = ...,
            DefaultMessage: "Campaign.Message" = ...,
            EmailMessage: "Campaign.CampaignEmailMessage" = ...,
            GCMMessage: "Campaign.Message" = ...,
            SMSMessage: "Campaign.CampaignSmsMessage" = ...
        ): ...
    class MetricDimension:
        def __init__(self, *, ComparisonOperator: str = ..., Value: float = ...): ...
    class QuietTime:
        def __init__(self, *, End: str, Start: str): ...
    class Schedule:
        def __init__(
            self,
            *,
            EndTime: str = ...,
            EventFilter: "Campaign.CampaignEventFilter" = ...,
            Frequency: str = ...,
            IsLocalTime: bool = ...,
            QuietTime: "Campaign.QuietTime" = ...,
            StartTime: str = ...,
            TimeZone: str = ...
        ): ...
    class SetDimension:
        def __init__(self, *, DimensionType: str = ..., Values: List[str] = ...): ...
    class WriteTreatmentResource:
        def __init__(
            self,
            *,
            MessageConfiguration: "Campaign.MessageConfiguration" = ...,
            Schedule: "Campaign.Schedule" = ...,
            SizePercent: int = ...,
            TreatmentDescription: str = ...,
            TreatmentName: str = ...
        ): ...

class EmailChannel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailchannel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        FromAddress: str,
        Identity: str,
        ConfigurationSet: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Enabled: bool = ...,
        RoleArn: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class EmailTemplate:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-emailtemplate.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Subject: str,
        TemplateName: str,
        DefaultSubstitutions: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        HtmlPart: str = ...,
        Tags: Any = ...,
        TemplateDescription: str = ...,
        TextPart: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class EventStream:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-eventstream.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        DestinationStreamArn: str,
        RoleArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class GCMChannel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-gcmchannel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiKey: str,
        ApplicationId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Enabled: bool = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class PushTemplate:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-pushtemplate.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        TemplateName: str,
        ADM: "PushTemplate.AndroidPushNotificationTemplate" = ...,
        APNS: "PushTemplate.APNSPushNotificationTemplate" = ...,
        Baidu: "PushTemplate.AndroidPushNotificationTemplate" = ...,
        Default: "PushTemplate.DefaultPushNotificationTemplate" = ...,
        DefaultSubstitutions: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        GCM: "PushTemplate.AndroidPushNotificationTemplate" = ...,
        Tags: Any = ...,
        TemplateDescription: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class APNSPushNotificationTemplate:
        def __init__(
            self,
            *,
            Action: str = ...,
            Body: str = ...,
            MediaUrl: str = ...,
            Sound: str = ...,
            Title: str = ...,
            Url: str = ...
        ): ...
    class AndroidPushNotificationTemplate:
        def __init__(
            self,
            *,
            Action: str = ...,
            Body: str = ...,
            ImageIconUrl: str = ...,
            ImageUrl: str = ...,
            SmallImageIconUrl: str = ...,
            Sound: str = ...,
            Title: str = ...,
            Url: str = ...
        ): ...
    class DefaultPushNotificationTemplate:
        def __init__(
            self,
            *,
            Action: str = ...,
            Body: str = ...,
            Sound: str = ...,
            Title: str = ...,
            Url: str = ...
        ): ...

class SMSChannel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Enabled: bool = ...,
        SenderId: str = ...,
        ShortCode: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Segment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-segment.html"""

    SegmentId: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Dimensions: "Segment.SegmentDimensions" = ...,
        SegmentGroups: "Segment.SegmentGroups" = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AttributeDimension:
        def __init__(self, *, AttributeType: str = ..., Values: List[str] = ...): ...
    class Behavior:
        def __init__(self, *, Recency: "Segment.Recency" = ...): ...
    class Coordinates:
        def __init__(self, *, Latitude: float, Longitude: float): ...
    class Demographic:
        def __init__(
            self,
            *,
            AppVersion: "Segment.SetDimension" = ...,
            Channel: "Segment.SetDimension" = ...,
            DeviceType: "Segment.SetDimension" = ...,
            Make: "Segment.SetDimension" = ...,
            Model: "Segment.SetDimension" = ...,
            Platform: "Segment.SetDimension" = ...
        ): ...
    class GPSPoint:
        def __init__(
            self, *, Coordinates: "Segment.Coordinates", RangeInKilometers: float
        ): ...
    class Groups:
        def __init__(
            self,
            *,
            Dimensions: List["Segment.SegmentDimensions"] = ...,
            SourceSegments: List["Segment.SourceSegments"] = ...,
            SourceType: str = ...,
            Type: str = ...
        ): ...
    class Location:
        def __init__(
            self,
            *,
            Country: "Segment.SetDimension" = ...,
            GPSPoint: "Segment.GPSPoint" = ...
        ): ...
    class Recency:
        def __init__(self, *, Duration: str, RecencyType: str): ...
    class SegmentDimensions:
        def __init__(
            self,
            *,
            Attributes: Any = ...,
            Behavior: "Segment.Behavior" = ...,
            Demographic: "Segment.Demographic" = ...,
            Location: "Segment.Location" = ...,
            Metrics: Any = ...,
            UserAttributes: Any = ...
        ): ...
    class SegmentGroups:
        def __init__(
            self, *, Groups: List["Segment.Groups"] = ..., Include: str = ...
        ): ...
    class SetDimension:
        def __init__(self, *, DimensionType: str = ..., Values: List[str] = ...): ...
    class SourceSegments:
        def __init__(self, *, Id: str, Version: int = ...): ...

class SmsTemplate:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smstemplate.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Body: str,
        TemplateName: str,
        DefaultSubstitutions: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: Any = ...,
        TemplateDescription: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class VoiceChannel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-voicechannel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Enabled: bool = ...,
        UpdateReplacePolicy: str = ...
    ): ...
