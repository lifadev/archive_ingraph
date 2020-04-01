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

_NAMESPACE = "AWS::SES"

class ConfigurationSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ConfigurationSetEventDestination:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ConfigurationSetName: str,
        EventDestination: "ConfigurationSetEventDestination.EventDestination",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
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
            Name: str = ...
        ): ...
    class KinesisFirehoseDestination:
        def __init__(self, *, DeliveryStreamARN: str, IAMRoleARN: str): ...

class ReceiptFilter:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Filter: "ReceiptFilter.Filter",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Filter:
        def __init__(self, *, IpFilter: "ReceiptFilter.IpFilter", Name: str = ...): ...
    class IpFilter:
        def __init__(self, *, Cidr: str, Policy: str): ...

class ReceiptRule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Rule: "ReceiptRule.Rule",
        RuleSetName: str,
        After: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Action:
        def __init__(
            self,
            *,
            AddHeaderAction: "ReceiptRule.AddHeaderAction" = ...,
            BounceAction: "ReceiptRule.BounceAction" = ...,
            LambdaAction: "ReceiptRule.LambdaAction" = ...,
            S3Action: "ReceiptRule.S3Action" = ...,
            SNSAction: "ReceiptRule.SNSAction" = ...,
            StopAction: "ReceiptRule.StopAction" = ...,
            WorkmailAction: "ReceiptRule.WorkmailAction" = ...
        ): ...
    class AddHeaderAction:
        def __init__(self, *, HeaderName: str, HeaderValue: str): ...
    class BounceAction:
        def __init__(
            self,
            *,
            Message: str,
            Sender: str,
            SmtpReplyCode: str,
            StatusCode: str = ...,
            TopicArn: str = ...
        ): ...
    class LambdaAction:
        def __init__(
            self, *, FunctionArn: str, InvocationType: str = ..., TopicArn: str = ...
        ): ...
    class Rule:
        def __init__(
            self,
            *,
            Actions: List["ReceiptRule.Action"] = ...,
            Enabled: bool = ...,
            Name: str = ...,
            Recipients: List[str] = ...,
            ScanEnabled: bool = ...,
            TlsPolicy: str = ...
        ): ...
    class S3Action:
        def __init__(
            self,
            *,
            BucketName: str,
            KmsKeyArn: str = ...,
            ObjectKeyPrefix: str = ...,
            TopicArn: str = ...
        ): ...
    class SNSAction:
        def __init__(self, *, Encoding: str = ..., TopicArn: str = ...): ...
    class StopAction:
        def __init__(self, *, Scope: str, TopicArn: str = ...): ...
    class WorkmailAction:
        def __init__(self, *, OrganizationArn: str, TopicArn: str = ...): ...

class ReceiptRuleSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RuleSetName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Template:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Template: "Template.Template_" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Template_:
        def __init__(
            self,
            *,
            HtmlPart: str = ...,
            SubjectPart: str = ...,
            TemplateName: str = ...,
            TextPart: str = ...
        ): ...
