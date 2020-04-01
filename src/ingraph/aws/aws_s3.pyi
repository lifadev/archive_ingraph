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

_NAMESPACE = "AWS::S3"

class AccessPoint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-accesspoint.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Bucket: str,
        CreationDate: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        NetworkOrigin: str = ...,
        Policy: Any = ...,
        PolicyStatus: Any = ...,
        PublicAccessBlockConfiguration: "AccessPoint.PublicAccessBlockConfiguration" = ...,
        UpdateReplacePolicy: str = ...,
        VpcConfiguration: "AccessPoint.VpcConfiguration" = ...
    ): ...
    class PublicAccessBlockConfiguration:
        def __init__(
            self,
            *,
            BlockPublicAcls: bool = ...,
            BlockPublicPolicy: bool = ...,
            IgnorePublicAcls: bool = ...,
            RestrictPublicBuckets: bool = ...
        ): ...
    class VpcConfiguration:
        def __init__(self, *, VpcId: str = ...): ...

class Bucket:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html"""

    Arn: Final[str]

    DomainName: Final[str]

    DualStackDomainName: Final[str]

    RegionalDomainName: Final[str]

    WebsiteURL: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AccelerateConfiguration: "Bucket.AccelerateConfiguration" = ...,
        AccessControl: str = ...,
        AnalyticsConfigurations: List["Bucket.AnalyticsConfiguration"] = ...,
        BucketEncryption: "Bucket.BucketEncryption" = ...,
        BucketName: str = ...,
        CorsConfiguration: "Bucket.CorsConfiguration" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InventoryConfigurations: List["Bucket.InventoryConfiguration"] = ...,
        LifecycleConfiguration: "Bucket.LifecycleConfiguration" = ...,
        LoggingConfiguration: "Bucket.LoggingConfiguration" = ...,
        MetricsConfigurations: List["Bucket.MetricsConfiguration"] = ...,
        NotificationConfiguration: "Bucket.NotificationConfiguration" = ...,
        ObjectLockConfiguration: "Bucket.ObjectLockConfiguration" = ...,
        ObjectLockEnabled: bool = ...,
        PublicAccessBlockConfiguration: "Bucket.PublicAccessBlockConfiguration" = ...,
        ReplicationConfiguration: "Bucket.ReplicationConfiguration" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VersioningConfiguration: "Bucket.VersioningConfiguration" = ...,
        WebsiteConfiguration: "Bucket.WebsiteConfiguration" = ...
    ): ...
    class AbortIncompleteMultipartUpload:
        def __init__(self, *, DaysAfterInitiation: int): ...
    class AccelerateConfiguration:
        def __init__(self, *, AccelerationStatus: str): ...
    class AccessControlTranslation:
        def __init__(self, *, Owner: str): ...
    class AnalyticsConfiguration:
        def __init__(
            self,
            *,
            Id: str,
            StorageClassAnalysis: "Bucket.StorageClassAnalysis",
            Prefix: str = ...,
            TagFilters: List["Bucket.TagFilter"] = ...
        ): ...
    class BucketEncryption:
        def __init__(
            self,
            *,
            ServerSideEncryptionConfiguration: List["Bucket.ServerSideEncryptionRule"]
        ): ...
    class CorsConfiguration:
        def __init__(self, *, CorsRules: List["Bucket.CorsRule"]): ...
    class CorsRule:
        def __init__(
            self,
            *,
            AllowedMethods: List[str],
            AllowedOrigins: List[str],
            AllowedHeaders: List[str] = ...,
            ExposedHeaders: List[str] = ...,
            Id: str = ...,
            MaxAge: int = ...
        ): ...
    class DataExport:
        def __init__(
            self, *, Destination: "Bucket.Destination", OutputSchemaVersion: str
        ): ...
    class DefaultRetention:
        def __init__(self, *, Days: int = ..., Mode: str = ..., Years: int = ...): ...
    class Destination:
        def __init__(
            self,
            *,
            BucketArn: str,
            Format: str,
            BucketAccountId: str = ...,
            Prefix: str = ...
        ): ...
    class EncryptionConfiguration:
        def __init__(self, *, ReplicaKmsKeyID: str): ...
    class FilterRule:
        def __init__(self, *, Name: str, Value: str): ...
    class InventoryConfiguration:
        def __init__(
            self,
            *,
            Destination: "Bucket.Destination",
            Enabled: bool,
            Id: str,
            IncludedObjectVersions: str,
            ScheduleFrequency: str,
            OptionalFields: List[str] = ...,
            Prefix: str = ...
        ): ...
    class LambdaConfiguration:
        def __init__(
            self,
            *,
            Event: str,
            Function: str,
            Filter: "Bucket.NotificationFilter" = ...
        ): ...
    class LifecycleConfiguration:
        def __init__(self, *, Rules: List["Bucket.Rule"]): ...
    class LoggingConfiguration:
        def __init__(
            self, *, DestinationBucketName: str = ..., LogFilePrefix: str = ...
        ): ...
    class MetricsConfiguration:
        def __init__(
            self,
            *,
            Id: str,
            Prefix: str = ...,
            TagFilters: List["Bucket.TagFilter"] = ...
        ): ...
    class NoncurrentVersionTransition:
        def __init__(self, *, StorageClass: str, TransitionInDays: int): ...
    class NotificationConfiguration:
        def __init__(
            self,
            *,
            LambdaConfigurations: List["Bucket.LambdaConfiguration"] = ...,
            QueueConfigurations: List["Bucket.QueueConfiguration"] = ...,
            TopicConfigurations: List["Bucket.TopicConfiguration"] = ...
        ): ...
    class NotificationFilter:
        def __init__(self, *, S3Key: "Bucket.S3KeyFilter"): ...
    class ObjectLockConfiguration:
        def __init__(
            self, *, ObjectLockEnabled: str = ..., Rule: "Bucket.ObjectLockRule" = ...
        ): ...
    class ObjectLockRule:
        def __init__(self, *, DefaultRetention: "Bucket.DefaultRetention" = ...): ...
    class PublicAccessBlockConfiguration:
        def __init__(
            self,
            *,
            BlockPublicAcls: bool = ...,
            BlockPublicPolicy: bool = ...,
            IgnorePublicAcls: bool = ...,
            RestrictPublicBuckets: bool = ...
        ): ...
    class QueueConfiguration:
        def __init__(
            self, *, Event: str, Queue: str, Filter: "Bucket.NotificationFilter" = ...
        ): ...
    class RedirectAllRequestsTo:
        def __init__(self, *, HostName: str, Protocol: str = ...): ...
    class RedirectRule:
        def __init__(
            self,
            *,
            HostName: str = ...,
            HttpRedirectCode: str = ...,
            Protocol: str = ...,
            ReplaceKeyPrefixWith: str = ...,
            ReplaceKeyWith: str = ...
        ): ...
    class ReplicationConfiguration:
        def __init__(self, *, Role: str, Rules: List["Bucket.ReplicationRule"]): ...
    class ReplicationDestination:
        def __init__(
            self,
            *,
            Bucket: str,
            AccessControlTranslation: "Bucket.AccessControlTranslation" = ...,
            Account: str = ...,
            EncryptionConfiguration: "Bucket.EncryptionConfiguration" = ...,
            StorageClass: str = ...
        ): ...
    class ReplicationRule:
        def __init__(
            self,
            *,
            Destination: "Bucket.ReplicationDestination",
            Prefix: str,
            Status: str,
            Id: str = ...,
            SourceSelectionCriteria: "Bucket.SourceSelectionCriteria" = ...
        ): ...
    class RoutingRule:
        def __init__(
            self,
            *,
            RedirectRule: "Bucket.RedirectRule",
            RoutingRuleCondition: "Bucket.RoutingRuleCondition" = ...
        ): ...
    class RoutingRuleCondition:
        def __init__(
            self, *, HttpErrorCodeReturnedEquals: str = ..., KeyPrefixEquals: str = ...
        ): ...
    class Rule:
        def __init__(
            self,
            *,
            Status: str,
            AbortIncompleteMultipartUpload: "Bucket.AbortIncompleteMultipartUpload" = ...,
            ExpirationDate: str = ...,
            ExpirationInDays: int = ...,
            Id: str = ...,
            NoncurrentVersionExpirationInDays: int = ...,
            NoncurrentVersionTransition: "Bucket.NoncurrentVersionTransition" = ...,
            NoncurrentVersionTransitions: List[
                "Bucket.NoncurrentVersionTransition"
            ] = ...,
            Prefix: str = ...,
            TagFilters: List["Bucket.TagFilter"] = ...,
            Transition: "Bucket.Transition" = ...,
            Transitions: List["Bucket.Transition"] = ...
        ): ...
    class S3KeyFilter:
        def __init__(self, *, Rules: List["Bucket.FilterRule"]): ...
    class ServerSideEncryptionByDefault:
        def __init__(self, *, SSEAlgorithm: str, KMSMasterKeyID: str = ...): ...
    class ServerSideEncryptionRule:
        def __init__(
            self,
            *,
            ServerSideEncryptionByDefault: "Bucket.ServerSideEncryptionByDefault" = ...
        ): ...
    class SourceSelectionCriteria:
        def __init__(
            self, *, SseKmsEncryptedObjects: "Bucket.SseKmsEncryptedObjects"
        ): ...
    class SseKmsEncryptedObjects:
        def __init__(self, *, Status: str): ...
    class StorageClassAnalysis:
        def __init__(self, *, DataExport: "Bucket.DataExport" = ...): ...
    class TagFilter:
        def __init__(self, *, Key: str, Value: str): ...
    class TopicConfiguration:
        def __init__(
            self, *, Event: str, Topic: str, Filter: "Bucket.NotificationFilter" = ...
        ): ...
    class Transition:
        def __init__(
            self,
            *,
            StorageClass: str,
            TransitionDate: str = ...,
            TransitionInDays: int = ...
        ): ...
    class VersioningConfiguration:
        def __init__(self, *, Status: str): ...
    class WebsiteConfiguration:
        def __init__(
            self,
            *,
            ErrorDocument: str = ...,
            IndexDocument: str = ...,
            RedirectAllRequestsTo: "Bucket.RedirectAllRequestsTo" = ...,
            RoutingRules: List["Bucket.RoutingRule"] = ...
        ): ...

class BucketPolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Bucket: str,
        PolicyDocument: Any,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
