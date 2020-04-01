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

_NAMESPACE = "AWS::KinesisFirehose"

class DeliveryStream:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DeliveryStreamName: str = ...,
        DeliveryStreamType: str = ...,
        DependsOn: List[Any] = ...,
        ElasticsearchDestinationConfiguration: "DeliveryStream.ElasticsearchDestinationConfiguration" = ...,
        ExtendedS3DestinationConfiguration: "DeliveryStream.ExtendedS3DestinationConfiguration" = ...,
        KinesisStreamSourceConfiguration: "DeliveryStream.KinesisStreamSourceConfiguration" = ...,
        RedshiftDestinationConfiguration: "DeliveryStream.RedshiftDestinationConfiguration" = ...,
        S3DestinationConfiguration: "DeliveryStream.S3DestinationConfiguration" = ...,
        SplunkDestinationConfiguration: "DeliveryStream.SplunkDestinationConfiguration" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class BufferingHints:
        def __init__(self, *, IntervalInSeconds: int, SizeInMBs: int): ...
    class CloudWatchLoggingOptions:
        def __init__(
            self,
            *,
            Enabled: bool = ...,
            LogGroupName: str = ...,
            LogStreamName: str = ...
        ): ...
    class CopyCommand:
        def __init__(
            self,
            *,
            DataTableName: str,
            CopyOptions: str = ...,
            DataTableColumns: str = ...
        ): ...
    class DataFormatConversionConfiguration:
        def __init__(
            self,
            *,
            Enabled: bool,
            InputFormatConfiguration: "DeliveryStream.InputFormatConfiguration",
            OutputFormatConfiguration: "DeliveryStream.OutputFormatConfiguration",
            SchemaConfiguration: "DeliveryStream.SchemaConfiguration"
        ): ...
    class Deserializer:
        def __init__(
            self,
            *,
            HiveJsonSerDe: "DeliveryStream.HiveJsonSerDe" = ...,
            OpenXJsonSerDe: "DeliveryStream.OpenXJsonSerDe" = ...
        ): ...
    class ElasticsearchBufferingHints:
        def __init__(self, *, IntervalInSeconds: int, SizeInMBs: int): ...
    class ElasticsearchDestinationConfiguration:
        def __init__(
            self,
            *,
            BufferingHints: "DeliveryStream.ElasticsearchBufferingHints",
            DomainARN: str,
            IndexName: str,
            IndexRotationPeriod: str,
            RetryOptions: "DeliveryStream.ElasticsearchRetryOptions",
            RoleARN: str,
            S3BackupMode: str,
            S3Configuration: "DeliveryStream.S3DestinationConfiguration",
            TypeName: str,
            CloudWatchLoggingOptions: "DeliveryStream.CloudWatchLoggingOptions" = ...,
            ProcessingConfiguration: "DeliveryStream.ProcessingConfiguration" = ...
        ): ...
    class ElasticsearchRetryOptions:
        def __init__(self, *, DurationInSeconds: int): ...
    class EncryptionConfiguration:
        def __init__(
            self,
            *,
            KMSEncryptionConfig: "DeliveryStream.KMSEncryptionConfig" = ...,
            NoEncryptionConfig: str = ...
        ): ...
    class ExtendedS3DestinationConfiguration:
        def __init__(
            self,
            *,
            BucketARN: str,
            BufferingHints: "DeliveryStream.BufferingHints",
            CompressionFormat: str,
            RoleARN: str,
            CloudWatchLoggingOptions: "DeliveryStream.CloudWatchLoggingOptions" = ...,
            DataFormatConversionConfiguration: "DeliveryStream.DataFormatConversionConfiguration" = ...,
            EncryptionConfiguration: "DeliveryStream.EncryptionConfiguration" = ...,
            ErrorOutputPrefix: str = ...,
            Prefix: str = ...,
            ProcessingConfiguration: "DeliveryStream.ProcessingConfiguration" = ...,
            S3BackupConfiguration: "DeliveryStream.S3DestinationConfiguration" = ...,
            S3BackupMode: str = ...
        ): ...
    class HiveJsonSerDe:
        def __init__(self, *, TimestampFormats: List[str] = ...): ...
    class InputFormatConfiguration:
        def __init__(self, *, Deserializer: "DeliveryStream.Deserializer"): ...
    class KMSEncryptionConfig:
        def __init__(self, *, AWSKMSKeyARN: str): ...
    class KinesisStreamSourceConfiguration:
        def __init__(self, *, KinesisStreamARN: str, RoleARN: str): ...
    class OpenXJsonSerDe:
        def __init__(
            self,
            *,
            CaseInsensitive: bool = ...,
            ColumnToJsonKeyMappings: Dict[str, str] = ...,
            ConvertDotsInJsonKeysToUnderscores: bool = ...
        ): ...
    class OrcSerDe:
        def __init__(
            self,
            *,
            BlockSizeBytes: int = ...,
            BloomFilterColumns: List[str] = ...,
            BloomFilterFalsePositiveProbability: float = ...,
            Compression: str = ...,
            DictionaryKeyThreshold: float = ...,
            EnablePadding: bool = ...,
            FormatVersion: str = ...,
            PaddingTolerance: float = ...,
            RowIndexStride: int = ...,
            StripeSizeBytes: int = ...
        ): ...
    class OutputFormatConfiguration:
        def __init__(self, *, Serializer: "DeliveryStream.Serializer"): ...
    class ParquetSerDe:
        def __init__(
            self,
            *,
            BlockSizeBytes: int = ...,
            Compression: str = ...,
            EnableDictionaryCompression: bool = ...,
            MaxPaddingBytes: int = ...,
            PageSizeBytes: int = ...,
            WriterVersion: str = ...
        ): ...
    class ProcessingConfiguration:
        def __init__(
            self,
            *,
            Enabled: bool = ...,
            Processors: List["DeliveryStream.Processor"] = ...
        ): ...
    class Processor:
        def __init__(
            self, *, Parameters: List["DeliveryStream.ProcessorParameter"], Type: str
        ): ...
    class ProcessorParameter:
        def __init__(self, *, ParameterName: str, ParameterValue: str): ...
    class RedshiftDestinationConfiguration:
        def __init__(
            self,
            *,
            ClusterJDBCURL: str,
            CopyCommand: "DeliveryStream.CopyCommand",
            Password: str,
            RoleARN: str,
            S3Configuration: "DeliveryStream.S3DestinationConfiguration",
            Username: str,
            CloudWatchLoggingOptions: "DeliveryStream.CloudWatchLoggingOptions" = ...,
            ProcessingConfiguration: "DeliveryStream.ProcessingConfiguration" = ...
        ): ...
    class S3DestinationConfiguration:
        def __init__(
            self,
            *,
            BucketARN: str,
            BufferingHints: "DeliveryStream.BufferingHints",
            CompressionFormat: str,
            RoleARN: str,
            CloudWatchLoggingOptions: "DeliveryStream.CloudWatchLoggingOptions" = ...,
            EncryptionConfiguration: "DeliveryStream.EncryptionConfiguration" = ...,
            ErrorOutputPrefix: str = ...,
            Prefix: str = ...
        ): ...
    class SchemaConfiguration:
        def __init__(
            self,
            *,
            CatalogId: str,
            DatabaseName: str,
            Region: str,
            RoleARN: str,
            TableName: str,
            VersionId: str
        ): ...
    class Serializer:
        def __init__(
            self,
            *,
            OrcSerDe: "DeliveryStream.OrcSerDe" = ...,
            ParquetSerDe: "DeliveryStream.ParquetSerDe" = ...
        ): ...
    class SplunkDestinationConfiguration:
        def __init__(
            self,
            *,
            HECEndpoint: str,
            HECEndpointType: str,
            HECToken: str,
            S3Configuration: "DeliveryStream.S3DestinationConfiguration",
            CloudWatchLoggingOptions: "DeliveryStream.CloudWatchLoggingOptions" = ...,
            HECAcknowledgmentTimeoutInSeconds: int = ...,
            ProcessingConfiguration: "DeliveryStream.ProcessingConfiguration" = ...,
            RetryOptions: "DeliveryStream.SplunkRetryOptions" = ...,
            S3BackupMode: str = ...
        ): ...
    class SplunkRetryOptions:
        def __init__(self, *, DurationInSeconds: int): ...
