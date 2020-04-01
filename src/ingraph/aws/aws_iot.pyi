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

_NAMESPACE = "AWS::IoT"

class Certificate:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-certificate.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        CertificateSigningRequest: str,
        Status: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Policy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policy.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        PolicyDocument: Any,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        PolicyName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class PolicyPrincipalAttachment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-policyprincipalattachment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PolicyName: str,
        Principal: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Thing:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thing.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AttributePayload: "Thing.AttributePayload" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ThingName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AttributePayload:
        def __init__(self, *, Attributes: Dict[str, str] = ...): ...

class ThingPrincipalAttachment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-thingprincipalattachment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Principal: str,
        ThingName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class TopicRule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iot-topicrule.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        TopicRulePayload: "TopicRule.TopicRulePayload",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RuleName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Action:
        def __init__(
            self,
            *,
            CloudwatchAlarm: "TopicRule.CloudwatchAlarmAction" = ...,
            CloudwatchMetric: "TopicRule.CloudwatchMetricAction" = ...,
            DynamoDB: "TopicRule.DynamoDBAction" = ...,
            DynamoDBv2: "TopicRule.DynamoDBv2Action" = ...,
            Elasticsearch: "TopicRule.ElasticsearchAction" = ...,
            Firehose: "TopicRule.FirehoseAction" = ...,
            Http: "TopicRule.HttpAction" = ...,
            IotAnalytics: "TopicRule.IotAnalyticsAction" = ...,
            IotEvents: "TopicRule.IotEventsAction" = ...,
            IotSiteWise: "TopicRule.IotSiteWiseAction" = ...,
            Kinesis: "TopicRule.KinesisAction" = ...,
            Lambda: "TopicRule.LambdaAction" = ...,
            Republish: "TopicRule.RepublishAction" = ...,
            S3: "TopicRule.S3Action" = ...,
            Sns: "TopicRule.SnsAction" = ...,
            Sqs: "TopicRule.SqsAction" = ...,
            StepFunctions: "TopicRule.StepFunctionsAction" = ...
        ): ...
    class AssetPropertyTimestamp:
        def __init__(self, *, TimeInSeconds: str, OffsetInNanos: str = ...): ...
    class AssetPropertyValue:
        def __init__(
            self,
            *,
            Timestamp: "TopicRule.AssetPropertyTimestamp",
            Value: "TopicRule.AssetPropertyVariant",
            Quality: str = ...
        ): ...
    class AssetPropertyVariant:
        def __init__(
            self,
            *,
            BooleanValue: str = ...,
            DoubleValue: str = ...,
            IntegerValue: str = ...,
            StringValue: str = ...
        ): ...
    class CloudwatchAlarmAction:
        def __init__(
            self, *, AlarmName: str, RoleArn: str, StateReason: str, StateValue: str
        ): ...
    class CloudwatchMetricAction:
        def __init__(
            self,
            *,
            MetricName: str,
            MetricNamespace: str,
            MetricUnit: str,
            MetricValue: str,
            RoleArn: str,
            MetricTimestamp: str = ...
        ): ...
    class DynamoDBAction:
        def __init__(
            self,
            *,
            HashKeyField: str,
            HashKeyValue: str,
            RoleArn: str,
            TableName: str,
            HashKeyType: str = ...,
            PayloadField: str = ...,
            RangeKeyField: str = ...,
            RangeKeyType: str = ...,
            RangeKeyValue: str = ...
        ): ...
    class DynamoDBv2Action:
        def __init__(
            self, *, PutItem: "TopicRule.PutItemInput" = ..., RoleArn: str = ...
        ): ...
    class ElasticsearchAction:
        def __init__(
            self, *, Endpoint: str, Id: str, Index: str, RoleArn: str, Type: str
        ): ...
    class FirehoseAction:
        def __init__(
            self, *, DeliveryStreamName: str, RoleArn: str, Separator: str = ...
        ): ...
    class HttpAction:
        def __init__(
            self,
            *,
            Url: str,
            Auth: "TopicRule.HttpAuthorization" = ...,
            ConfirmationUrl: str = ...,
            Headers: List["TopicRule.HttpActionHeader"] = ...
        ): ...
    class HttpActionHeader:
        def __init__(self, *, Key: str, Value: str): ...
    class HttpAuthorization:
        def __init__(self, *, Sigv4: "TopicRule.SigV4Authorization" = ...): ...
    class IotAnalyticsAction:
        def __init__(self, *, ChannelName: str, RoleArn: str): ...
    class IotEventsAction:
        def __init__(self, *, InputName: str, RoleArn: str, MessageId: str = ...): ...
    class IotSiteWiseAction:
        def __init__(
            self,
            *,
            PutAssetPropertyValueEntries: List["TopicRule.PutAssetPropertyValueEntry"],
            RoleArn: str
        ): ...
    class KinesisAction:
        def __init__(
            self, *, RoleArn: str, StreamName: str, PartitionKey: str = ...
        ): ...
    class LambdaAction:
        def __init__(self, *, FunctionArn: str = ...): ...
    class PutAssetPropertyValueEntry:
        def __init__(
            self,
            *,
            PropertyValues: List["TopicRule.AssetPropertyValue"],
            AssetId: str = ...,
            EntryId: str = ...,
            PropertyAlias: str = ...,
            PropertyId: str = ...
        ): ...
    class PutItemInput:
        def __init__(self, *, TableName: str): ...
    class RepublishAction:
        def __init__(self, *, RoleArn: str, Topic: str, Qos: int = ...): ...
    class S3Action:
        def __init__(self, *, BucketName: str, Key: str, RoleArn: str): ...
    class SigV4Authorization:
        def __init__(self, *, RoleArn: str, ServiceName: str, SigningRegion: str): ...
    class SnsAction:
        def __init__(
            self, *, RoleArn: str, TargetArn: str, MessageFormat: str = ...
        ): ...
    class SqsAction:
        def __init__(self, *, QueueUrl: str, RoleArn: str, UseBase64: bool = ...): ...
    class StepFunctionsAction:
        def __init__(
            self, *, RoleArn: str, StateMachineName: str, ExecutionNamePrefix: str = ...
        ): ...
    class TopicRulePayload:
        def __init__(
            self,
            *,
            Actions: List["TopicRule.Action"],
            RuleDisabled: bool,
            Sql: str,
            AwsIotSqlVersion: str = ...,
            Description: str = ...,
            ErrorAction: "TopicRule.Action" = ...
        ): ...
