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

_NAMESPACE = "AWS::KinesisAnalyticsV2"

class Application:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-application.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        RuntimeEnvironment: str,
        ServiceExecutionRole: str,
        ApplicationConfiguration: "Application.ApplicationConfiguration" = ...,
        ApplicationDescription: str = ...,
        ApplicationName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ApplicationCodeConfiguration:
        def __init__(
            self, *, CodeContent: "Application.CodeContent", CodeContentType: str
        ): ...
    class ApplicationConfiguration:
        def __init__(
            self,
            *,
            ApplicationCodeConfiguration: "Application.ApplicationCodeConfiguration" = ...,
            ApplicationSnapshotConfiguration: "Application.ApplicationSnapshotConfiguration" = ...,
            EnvironmentProperties: "Application.EnvironmentProperties" = ...,
            FlinkApplicationConfiguration: "Application.FlinkApplicationConfiguration" = ...,
            SqlApplicationConfiguration: "Application.SqlApplicationConfiguration" = ...
        ): ...
    class ApplicationSnapshotConfiguration:
        def __init__(self, *, SnapshotsEnabled: bool): ...
    class CSVMappingParameters:
        def __init__(self, *, RecordColumnDelimiter: str, RecordRowDelimiter: str): ...
    class CheckpointConfiguration:
        def __init__(
            self,
            *,
            ConfigurationType: str,
            CheckpointInterval: int = ...,
            CheckpointingEnabled: bool = ...,
            MinPauseBetweenCheckpoints: int = ...
        ): ...
    class CodeContent:
        def __init__(
            self,
            *,
            S3ContentLocation: "Application.S3ContentLocation" = ...,
            TextContent: str = ...,
            ZipFileContent: str = ...
        ): ...
    class EnvironmentProperties:
        def __init__(
            self, *, PropertyGroups: List["Application.PropertyGroup"] = ...
        ): ...
    class FlinkApplicationConfiguration:
        def __init__(
            self,
            *,
            CheckpointConfiguration: "Application.CheckpointConfiguration" = ...,
            MonitoringConfiguration: "Application.MonitoringConfiguration" = ...,
            ParallelismConfiguration: "Application.ParallelismConfiguration" = ...
        ): ...
    class Input:
        def __init__(
            self,
            *,
            InputSchema: "Application.InputSchema",
            NamePrefix: str,
            InputParallelism: "Application.InputParallelism" = ...,
            InputProcessingConfiguration: "Application.InputProcessingConfiguration" = ...,
            KinesisFirehoseInput: "Application.KinesisFirehoseInput" = ...,
            KinesisStreamsInput: "Application.KinesisStreamsInput" = ...
        ): ...
    class InputLambdaProcessor:
        def __init__(self, *, ResourceARN: str): ...
    class InputParallelism:
        def __init__(self, *, Count: int = ...): ...
    class InputProcessingConfiguration:
        def __init__(
            self, *, InputLambdaProcessor: "Application.InputLambdaProcessor" = ...
        ): ...
    class InputSchema:
        def __init__(
            self,
            *,
            RecordColumns: List["Application.RecordColumn"],
            RecordFormat: "Application.RecordFormat",
            RecordEncoding: str = ...
        ): ...
    class JSONMappingParameters:
        def __init__(self, *, RecordRowPath: str): ...
    class KinesisFirehoseInput:
        def __init__(self, *, ResourceARN: str): ...
    class KinesisStreamsInput:
        def __init__(self, *, ResourceARN: str): ...
    class MappingParameters:
        def __init__(
            self,
            *,
            CSVMappingParameters: "Application.CSVMappingParameters" = ...,
            JSONMappingParameters: "Application.JSONMappingParameters" = ...
        ): ...
    class MonitoringConfiguration:
        def __init__(
            self,
            *,
            ConfigurationType: str,
            LogLevel: str = ...,
            MetricsLevel: str = ...
        ): ...
    class ParallelismConfiguration:
        def __init__(
            self,
            *,
            ConfigurationType: str,
            AutoScalingEnabled: bool = ...,
            Parallelism: int = ...,
            ParallelismPerKPU: int = ...
        ): ...
    class PropertyGroup:
        def __init__(self, *, PropertyGroupId: str = ..., PropertyMap: Any = ...): ...
    class RecordColumn:
        def __init__(self, *, Name: str, SqlType: str, Mapping: str = ...): ...
    class RecordFormat:
        def __init__(
            self,
            *,
            RecordFormatType: str,
            MappingParameters: "Application.MappingParameters" = ...
        ): ...
    class S3ContentLocation:
        def __init__(
            self, *, BucketARN: str = ..., FileKey: str = ..., ObjectVersion: str = ...
        ): ...
    class SqlApplicationConfiguration:
        def __init__(self, *, Inputs: List["Application.Input"] = ...): ...

class ApplicationCloudWatchLoggingOption:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationcloudwatchloggingoption.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationName: str,
        CloudWatchLoggingOption: "ApplicationCloudWatchLoggingOption.CloudWatchLoggingOption",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CloudWatchLoggingOption:
        def __init__(self, *, LogStreamARN: str): ...

class ApplicationOutput:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationoutput.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationName: str,
        Output: "ApplicationOutput.Output",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DestinationSchema:
        def __init__(self, *, RecordFormatType: str = ...): ...
    class KinesisFirehoseOutput:
        def __init__(self, *, ResourceARN: str): ...
    class KinesisStreamsOutput:
        def __init__(self, *, ResourceARN: str): ...
    class LambdaOutput:
        def __init__(self, *, ResourceARN: str): ...
    class Output:
        def __init__(
            self,
            *,
            DestinationSchema: "ApplicationOutput.DestinationSchema",
            KinesisFirehoseOutput: "ApplicationOutput.KinesisFirehoseOutput" = ...,
            KinesisStreamsOutput: "ApplicationOutput.KinesisStreamsOutput" = ...,
            LambdaOutput: "ApplicationOutput.LambdaOutput" = ...,
            Name: str = ...
        ): ...

class ApplicationReferenceDataSource:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalyticsv2-applicationreferencedatasource.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationName: str,
        ReferenceDataSource: "ApplicationReferenceDataSource.ReferenceDataSource",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CSVMappingParameters:
        def __init__(self, *, RecordColumnDelimiter: str, RecordRowDelimiter: str): ...
    class JSONMappingParameters:
        def __init__(self, *, RecordRowPath: str): ...
    class MappingParameters:
        def __init__(
            self,
            *,
            CSVMappingParameters: "ApplicationReferenceDataSource.CSVMappingParameters" = ...,
            JSONMappingParameters: "ApplicationReferenceDataSource.JSONMappingParameters" = ...
        ): ...
    class RecordColumn:
        def __init__(self, *, Name: str, SqlType: str, Mapping: str = ...): ...
    class RecordFormat:
        def __init__(
            self,
            *,
            RecordFormatType: str,
            MappingParameters: "ApplicationReferenceDataSource.MappingParameters" = ...
        ): ...
    class ReferenceDataSource:
        def __init__(
            self,
            *,
            ReferenceSchema: "ApplicationReferenceDataSource.ReferenceSchema",
            S3ReferenceDataSource: "ApplicationReferenceDataSource.S3ReferenceDataSource" = ...,
            TableName: str = ...
        ): ...
    class ReferenceSchema:
        def __init__(
            self,
            *,
            RecordColumns: List["ApplicationReferenceDataSource.RecordColumn"],
            RecordFormat: "ApplicationReferenceDataSource.RecordFormat",
            RecordEncoding: str = ...
        ): ...
    class S3ReferenceDataSource:
        def __init__(self, *, BucketARN: str, FileKey: str): ...
