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

_NAMESPACE = "AWS::DMS"

class Certificate:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CertificateIdentifier: str = ...,
        CertificatePem: str = ...,
        CertificateWallet: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Endpoint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html"""

    ExternalId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        EndpointType: str,
        EngineName: str,
        CertificateArn: str = ...,
        DatabaseName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DynamoDbSettings: "Endpoint.DynamoDbSettings" = ...,
        ElasticsearchSettings: "Endpoint.ElasticsearchSettings" = ...,
        EndpointIdentifier: str = ...,
        ExtraConnectionAttributes: str = ...,
        KafkaSettings: "Endpoint.KafkaSettings" = ...,
        KinesisSettings: "Endpoint.KinesisSettings" = ...,
        KmsKeyId: str = ...,
        MongoDbSettings: "Endpoint.MongoDbSettings" = ...,
        Password: str = ...,
        Port: int = ...,
        S3Settings: "Endpoint.S3Settings" = ...,
        ServerName: str = ...,
        SslMode: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        Username: str = ...
    ): ...
    class DynamoDbSettings:
        def __init__(self, *, ServiceAccessRoleArn: str = ...): ...
    class ElasticsearchSettings:
        def __init__(
            self,
            *,
            EndpointUri: str = ...,
            ErrorRetryDuration: int = ...,
            FullLoadErrorPercentage: int = ...,
            ServiceAccessRoleArn: str = ...
        ): ...
    class KafkaSettings:
        def __init__(self, *, Broker: str = ..., Topic: str = ...): ...
    class KinesisSettings:
        def __init__(
            self,
            *,
            MessageFormat: str = ...,
            ServiceAccessRoleArn: str = ...,
            StreamArn: str = ...
        ): ...
    class MongoDbSettings:
        def __init__(
            self,
            *,
            AuthMechanism: str = ...,
            AuthSource: str = ...,
            AuthType: str = ...,
            DatabaseName: str = ...,
            DocsToInvestigate: str = ...,
            ExtractDocId: str = ...,
            NestingLevel: str = ...,
            Password: str = ...,
            Port: int = ...,
            ServerName: str = ...,
            Username: str = ...
        ): ...
    class S3Settings:
        def __init__(
            self,
            *,
            BucketFolder: str = ...,
            BucketName: str = ...,
            CompressionType: str = ...,
            CsvDelimiter: str = ...,
            CsvRowDelimiter: str = ...,
            ExternalTableDefinition: str = ...,
            ServiceAccessRoleArn: str = ...
        ): ...

class EventSubscription:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        SnsTopicArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Enabled: bool = ...,
        EventCategories: List[str] = ...,
        SourceIds: List[str] = ...,
        SourceType: str = ...,
        SubscriptionName: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ReplicationInstance:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html"""

    ReplicationInstancePublicIpAddresses: Final[List[str]]

    ReplicationInstancePrivateIpAddresses: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ReplicationInstanceClass: str,
        AllocatedStorage: int = ...,
        AllowMajorVersionUpgrade: bool = ...,
        AutoMinorVersionUpgrade: bool = ...,
        AvailabilityZone: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EngineVersion: str = ...,
        KmsKeyId: str = ...,
        MultiAZ: bool = ...,
        PreferredMaintenanceWindow: str = ...,
        PubliclyAccessible: bool = ...,
        ReplicationInstanceIdentifier: str = ...,
        ReplicationSubnetGroupIdentifier: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VpcSecurityGroupIds: List[str] = ...
    ): ...

class ReplicationSubnetGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ReplicationSubnetGroupDescription: str,
        SubnetIds: List[str],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ReplicationSubnetGroupIdentifier: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ReplicationTask:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        MigrationType: str,
        ReplicationInstanceArn: str,
        SourceEndpointArn: str,
        TableMappings: str,
        TargetEndpointArn: str,
        CdcStartPosition: str = ...,
        CdcStartTime: float = ...,
        CdcStopPosition: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ReplicationTaskIdentifier: str = ...,
        ReplicationTaskSettings: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
