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

_NAMESPACE = "AWS::KinesisAnalytics"

class Application:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-application.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Inputs: List["Application.Input"],
        ApplicationCode: str = ...,
        ApplicationDescription: str = ...,
        ApplicationName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CSVMappingParameters:
        def __init__(self, *, RecordColumnDelimiter: str, RecordRowDelimiter: str): ...
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
        def __init__(self, *, ResourceARN: str, RoleARN: str): ...
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
        def __init__(self, *, ResourceARN: str, RoleARN: str): ...
    class KinesisStreamsInput:
        def __init__(self, *, ResourceARN: str, RoleARN: str): ...
    class MappingParameters:
        def __init__(
            self,
            *,
            CSVMappingParameters: "Application.CSVMappingParameters" = ...,
            JSONMappingParameters: "Application.JSONMappingParameters" = ...
        ): ...
    class RecordColumn:
        def __init__(self, *, Name: str, SqlType: str, Mapping: str = ...): ...
    class RecordFormat:
        def __init__(
            self,
            *,
            RecordFormatType: str,
            MappingParameters: "Application.MappingParameters" = ...
        ): ...

class ApplicationOutput:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationoutput.html"""

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
        def __init__(self, *, ResourceARN: str, RoleARN: str): ...
    class KinesisStreamsOutput:
        def __init__(self, *, ResourceARN: str, RoleARN: str): ...
    class LambdaOutput:
        def __init__(self, *, ResourceARN: str, RoleARN: str): ...
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
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisanalytics-applicationreferencedatasource.html"""

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
        def __init__(self, *, BucketARN: str, FileKey: str, ReferenceRoleARN: str): ...
