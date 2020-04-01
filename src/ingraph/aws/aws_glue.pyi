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

_NAMESPACE = "AWS::Glue"

class Classifier:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-classifier.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CsvClassifier: "Classifier.CsvClassifier" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        GrokClassifier: "Classifier.GrokClassifier" = ...,
        JsonClassifier: "Classifier.JsonClassifier" = ...,
        UpdateReplacePolicy: str = ...,
        XMLClassifier: "Classifier.XMLClassifier" = ...
    ): ...
    class CsvClassifier:
        def __init__(
            self,
            *,
            AllowSingleColumn: bool = ...,
            ContainsHeader: str = ...,
            Delimiter: str = ...,
            DisableValueTrimming: bool = ...,
            Header: List[str] = ...,
            Name: str = ...,
            QuoteSymbol: str = ...
        ): ...
    class GrokClassifier:
        def __init__(
            self,
            *,
            Classification: str,
            GrokPattern: str,
            CustomPatterns: str = ...,
            Name: str = ...
        ): ...
    class JsonClassifier:
        def __init__(self, *, JsonPath: str, Name: str = ...): ...
    class XMLClassifier:
        def __init__(self, *, Classification: str, RowTag: str, Name: str = ...): ...

class Connection:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-connection.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CatalogId: str,
        ConnectionInput: "Connection.ConnectionInput",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ConnectionInput:
        def __init__(
            self,
            *,
            ConnectionProperties: Any,
            ConnectionType: str,
            Description: str = ...,
            MatchCriteria: List[str] = ...,
            Name: str = ...,
            PhysicalConnectionRequirements: "Connection.PhysicalConnectionRequirements" = ...
        ): ...
    class PhysicalConnectionRequirements:
        def __init__(
            self,
            *,
            AvailabilityZone: str = ...,
            SecurityGroupIdList: List[str] = ...,
            SubnetId: str = ...
        ): ...

class Crawler:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-crawler.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Role: str,
        Targets: "Crawler.Targets",
        Classifiers: List[str] = ...,
        Configuration: str = ...,
        CrawlerSecurityConfiguration: str = ...,
        DatabaseName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Name: str = ...,
        Schedule: "Crawler.Schedule" = ...,
        SchemaChangePolicy: "Crawler.SchemaChangePolicy" = ...,
        TablePrefix: str = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CatalogTarget:
        def __init__(self, *, DatabaseName: str = ..., Tables: List[str] = ...): ...
    class DynamoDBTarget:
        def __init__(self, *, Path: str = ...): ...
    class JdbcTarget:
        def __init__(
            self,
            *,
            ConnectionName: str = ...,
            Exclusions: List[str] = ...,
            Path: str = ...
        ): ...
    class S3Target:
        def __init__(self, *, Exclusions: List[str] = ..., Path: str = ...): ...
    class Schedule:
        def __init__(self, *, ScheduleExpression: str = ...): ...
    class SchemaChangePolicy:
        def __init__(self, *, DeleteBehavior: str = ..., UpdateBehavior: str = ...): ...
    class Targets:
        def __init__(
            self,
            *,
            CatalogTargets: List["Crawler.CatalogTarget"] = ...,
            DynamoDBTargets: List["Crawler.DynamoDBTarget"] = ...,
            JdbcTargets: List["Crawler.JdbcTarget"] = ...,
            S3Targets: List["Crawler.S3Target"] = ...
        ): ...

class DataCatalogEncryptionSettings:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-datacatalogencryptionsettings.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CatalogId: str,
        DataCatalogEncryptionSettings: "DataCatalogEncryptionSettings.DataCatalogEncryptionSettings_",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ConnectionPasswordEncryption:
        def __init__(
            self, *, KmsKeyId: str = ..., ReturnConnectionPasswordEncrypted: bool = ...
        ): ...
    class DataCatalogEncryptionSettings_:
        def __init__(
            self,
            *,
            ConnectionPasswordEncryption: "DataCatalogEncryptionSettings.ConnectionPasswordEncryption" = ...,
            EncryptionAtRest: "DataCatalogEncryptionSettings.EncryptionAtRest" = ...
        ): ...
    class EncryptionAtRest:
        def __init__(
            self, *, CatalogEncryptionMode: str = ..., SseAwsKmsKeyId: str = ...
        ): ...

class Database:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-database.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CatalogId: str,
        DatabaseInput: "Database.DatabaseInput",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DatabaseInput:
        def __init__(
            self,
            *,
            Description: str = ...,
            LocationUri: str = ...,
            Name: str = ...,
            Parameters: Any = ...
        ): ...

class DevEndpoint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-devendpoint.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        RoleArn: str,
        Arguments: Any = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EndpointName: str = ...,
        ExtraJarsS3Path: str = ...,
        ExtraPythonLibsS3Path: str = ...,
        GlueVersion: str = ...,
        NumberOfNodes: int = ...,
        NumberOfWorkers: int = ...,
        PublicKey: str = ...,
        SecurityConfiguration: str = ...,
        SecurityGroupIds: List[str] = ...,
        SubnetId: str = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...,
        WorkerType: str = ...
    ): ...

class Job:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-job.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Command: "Job.JobCommand",
        Role: str,
        AllocatedCapacity: float = ...,
        Connections: "Job.ConnectionsList" = ...,
        DefaultArguments: Any = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        ExecutionProperty: "Job.ExecutionProperty" = ...,
        GlueVersion: str = ...,
        LogUri: str = ...,
        MaxCapacity: float = ...,
        MaxRetries: float = ...,
        Name: str = ...,
        NotificationProperty: "Job.NotificationProperty" = ...,
        NumberOfWorkers: int = ...,
        SecurityConfiguration: str = ...,
        Tags: Any = ...,
        Timeout: int = ...,
        UpdateReplacePolicy: str = ...,
        WorkerType: str = ...
    ): ...
    class ConnectionsList:
        def __init__(self, *, Connections: List[str] = ...): ...
    class ExecutionProperty:
        def __init__(self, *, MaxConcurrentRuns: float = ...): ...
    class JobCommand:
        def __init__(
            self,
            *,
            Name: str = ...,
            PythonVersion: str = ...,
            ScriptLocation: str = ...
        ): ...
    class NotificationProperty:
        def __init__(self, *, NotifyDelayAfter: int = ...): ...

class MLTransform:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-mltransform.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        InputRecordTables: "MLTransform.InputRecordTables",
        Role: str,
        TransformParameters: "MLTransform.TransformParameters",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        GlueVersion: str = ...,
        MaxCapacity: float = ...,
        MaxRetries: int = ...,
        Name: str = ...,
        NumberOfWorkers: int = ...,
        Timeout: int = ...,
        UpdateReplacePolicy: str = ...,
        WorkerType: str = ...
    ): ...
    class FindMatchesParameters:
        def __init__(
            self,
            *,
            PrimaryKeyColumnName: str,
            AccuracyCostTradeoff: float = ...,
            EnforceProvidedLabels: bool = ...,
            PrecisionRecallTradeoff: float = ...
        ): ...
    class GlueTables:
        def __init__(
            self,
            *,
            DatabaseName: str,
            TableName: str,
            CatalogId: str = ...,
            ConnectionName: str = ...
        ): ...
    class InputRecordTables:
        def __init__(self, *, GlueTables: List["MLTransform.GlueTables"] = ...): ...
    class TransformParameters:
        def __init__(
            self,
            *,
            TransformType: str,
            FindMatchesParameters: "MLTransform.FindMatchesParameters" = ...
        ): ...

class Partition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-partition.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CatalogId: str,
        DatabaseName: str,
        PartitionInput: "Partition.PartitionInput",
        TableName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Column:
        def __init__(self, *, Name: str, Comment: str = ..., Type: str = ...): ...
    class Order:
        def __init__(self, *, Column: str, SortOrder: int = ...): ...
    class PartitionInput:
        def __init__(
            self,
            *,
            Values: List[str],
            Parameters: Any = ...,
            StorageDescriptor: "Partition.StorageDescriptor" = ...
        ): ...
    class SerdeInfo:
        def __init__(
            self,
            *,
            Name: str = ...,
            Parameters: Any = ...,
            SerializationLibrary: str = ...
        ): ...
    class SkewedInfo:
        def __init__(
            self,
            *,
            SkewedColumnNames: List[str] = ...,
            SkewedColumnValueLocationMaps: Any = ...,
            SkewedColumnValues: List[str] = ...
        ): ...
    class StorageDescriptor:
        def __init__(
            self,
            *,
            BucketColumns: List[str] = ...,
            Columns: List["Partition.Column"] = ...,
            Compressed: bool = ...,
            InputFormat: str = ...,
            Location: str = ...,
            NumberOfBuckets: int = ...,
            OutputFormat: str = ...,
            Parameters: Any = ...,
            SerdeInfo: "Partition.SerdeInfo" = ...,
            SkewedInfo: "Partition.SkewedInfo" = ...,
            SortColumns: List["Partition.Order"] = ...,
            StoredAsSubDirectories: bool = ...
        ): ...

class SecurityConfiguration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-securityconfiguration.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        EncryptionConfiguration: "SecurityConfiguration.EncryptionConfiguration",
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CloudWatchEncryption:
        def __init__(
            self, *, CloudWatchEncryptionMode: str = ..., KmsKeyArn: str = ...
        ): ...
    class EncryptionConfiguration:
        def __init__(
            self,
            *,
            CloudWatchEncryption: "SecurityConfiguration.CloudWatchEncryption" = ...,
            JobBookmarksEncryption: "SecurityConfiguration.JobBookmarksEncryption" = ...,
            S3Encryptions: "SecurityConfiguration.S3Encryptions" = ...
        ): ...
    class JobBookmarksEncryption:
        def __init__(
            self, *, JobBookmarksEncryptionMode: str = ..., KmsKeyArn: str = ...
        ): ...
    class S3Encryption:
        def __init__(self, *, KmsKeyArn: str = ..., S3EncryptionMode: str = ...): ...
    class S3Encryptions:
        def __init__(self) -> None: ...

class Table:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-table.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CatalogId: str,
        DatabaseName: str,
        TableInput: "Table.TableInput",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Column:
        def __init__(self, *, Name: str, Comment: str = ..., Type: str = ...): ...
    class Order:
        def __init__(self, *, Column: str, SortOrder: int): ...
    class SerdeInfo:
        def __init__(
            self,
            *,
            Name: str = ...,
            Parameters: Any = ...,
            SerializationLibrary: str = ...
        ): ...
    class SkewedInfo:
        def __init__(
            self,
            *,
            SkewedColumnNames: List[str] = ...,
            SkewedColumnValueLocationMaps: Any = ...,
            SkewedColumnValues: List[str] = ...
        ): ...
    class StorageDescriptor:
        def __init__(
            self,
            *,
            BucketColumns: List[str] = ...,
            Columns: List["Table.Column"] = ...,
            Compressed: bool = ...,
            InputFormat: str = ...,
            Location: str = ...,
            NumberOfBuckets: int = ...,
            OutputFormat: str = ...,
            Parameters: Any = ...,
            SerdeInfo: "Table.SerdeInfo" = ...,
            SkewedInfo: "Table.SkewedInfo" = ...,
            SortColumns: List["Table.Order"] = ...,
            StoredAsSubDirectories: bool = ...
        ): ...
    class TableInput:
        def __init__(
            self,
            *,
            Description: str = ...,
            Name: str = ...,
            Owner: str = ...,
            Parameters: Any = ...,
            PartitionKeys: List["Table.Column"] = ...,
            Retention: int = ...,
            StorageDescriptor: "Table.StorageDescriptor" = ...,
            TableType: str = ...,
            ViewExpandedText: str = ...,
            ViewOriginalText: str = ...
        ): ...

class Trigger:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-trigger.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Actions: List["Trigger.Action"],
        Type: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Name: str = ...,
        Predicate: "Trigger.Predicate" = ...,
        Schedule: str = ...,
        StartOnCreation: bool = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...,
        WorkflowName: str = ...
    ): ...
    class Action:
        def __init__(
            self,
            *,
            Arguments: Any = ...,
            CrawlerName: str = ...,
            JobName: str = ...,
            NotificationProperty: "Trigger.NotificationProperty" = ...,
            SecurityConfiguration: str = ...,
            Timeout: int = ...
        ): ...
    class Condition:
        def __init__(
            self,
            *,
            CrawlState: str = ...,
            CrawlerName: str = ...,
            JobName: str = ...,
            LogicalOperator: str = ...,
            State: str = ...
        ): ...
    class NotificationProperty:
        def __init__(self, *, NotifyDelayAfter: int = ...): ...
    class Predicate:
        def __init__(
            self, *, Conditions: List["Trigger.Condition"] = ..., Logical: str = ...
        ): ...

class Workflow:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-workflow.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DefaultRunProperties: Any = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Name: str = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
