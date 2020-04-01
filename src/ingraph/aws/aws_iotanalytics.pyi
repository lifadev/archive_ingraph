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

_NAMESPACE = "AWS::IoTAnalytics"

class Channel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-channel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ChannelName: str = ...,
        ChannelStorage: "Channel.ChannelStorage" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RetentionPeriod: "Channel.RetentionPeriod" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ChannelStorage:
        def __init__(
            self,
            *,
            CustomerManagedS3: "Channel.CustomerManagedS3" = ...,
            ServiceManagedS3: "Channel.ServiceManagedS3" = ...
        ): ...
    class CustomerManagedS3:
        def __init__(self, *, Bucket: str, RoleArn: str, KeyPrefix: str = ...): ...
    class RetentionPeriod:
        def __init__(self, *, NumberOfDays: int = ..., Unlimited: bool = ...): ...
    class ServiceManagedS3:
        def __init__(self) -> None: ...

class Dataset:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-dataset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Actions: List["Dataset.Action"],
        ContentDeliveryRules: List["Dataset.DatasetContentDeliveryRule"] = ...,
        DatasetName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RetentionPeriod: "Dataset.RetentionPeriod" = ...,
        Tags: List["Tag"] = ...,
        Triggers: List["Dataset.Trigger"] = ...,
        UpdateReplacePolicy: str = ...,
        VersioningConfiguration: "Dataset.VersioningConfiguration" = ...
    ): ...
    class Action:
        def __init__(
            self,
            *,
            ActionName: str,
            ContainerAction: "Dataset.ContainerAction" = ...,
            QueryAction: "Dataset.QueryAction" = ...
        ): ...
    class ContainerAction:
        def __init__(
            self,
            *,
            ExecutionRoleArn: str,
            Image: str,
            ResourceConfiguration: "Dataset.ResourceConfiguration",
            Variables: List["Dataset.Variable"] = ...
        ): ...
    class DatasetContentDeliveryRule:
        def __init__(
            self,
            *,
            Destination: "Dataset.DatasetContentDeliveryRuleDestination",
            EntryName: str = ...
        ): ...
    class DatasetContentDeliveryRuleDestination:
        def __init__(
            self,
            *,
            IotEventsDestinationConfiguration: "Dataset.IotEventsDestinationConfiguration" = ...,
            S3DestinationConfiguration: "Dataset.S3DestinationConfiguration" = ...
        ): ...
    class DatasetContentVersionValue:
        def __init__(self, *, DatasetName: str = ...): ...
    class DeltaTime:
        def __init__(self, *, OffsetSeconds: int, TimeExpression: str): ...
    class Filter:
        def __init__(self, *, DeltaTime: "Dataset.DeltaTime" = ...): ...
    class GlueConfiguration:
        def __init__(self, *, DatabaseName: str, TableName: str): ...
    class IotEventsDestinationConfiguration:
        def __init__(self, *, InputName: str, RoleArn: str): ...
    class OutputFileUriValue:
        def __init__(self, *, FileName: str = ...): ...
    class QueryAction:
        def __init__(self, *, SqlQuery: str, Filters: List["Dataset.Filter"] = ...): ...
    class ResourceConfiguration:
        def __init__(self, *, ComputeType: str, VolumeSizeInGB: int): ...
    class RetentionPeriod:
        def __init__(self, *, NumberOfDays: int, Unlimited: bool): ...
    class S3DestinationConfiguration:
        def __init__(
            self,
            *,
            Bucket: str,
            Key: str,
            RoleArn: str,
            GlueConfiguration: "Dataset.GlueConfiguration" = ...
        ): ...
    class Schedule:
        def __init__(self, *, ScheduleExpression: str): ...
    class Trigger:
        def __init__(
            self,
            *,
            Schedule: "Dataset.Schedule" = ...,
            TriggeringDataset: "Dataset.TriggeringDataset" = ...
        ): ...
    class TriggeringDataset:
        def __init__(self, *, DatasetName: str): ...
    class Variable:
        def __init__(
            self,
            *,
            VariableName: str,
            DatasetContentVersionValue: "Dataset.DatasetContentVersionValue" = ...,
            DoubleValue: float = ...,
            OutputFileUriValue: "Dataset.OutputFileUriValue" = ...,
            StringValue: str = ...
        ): ...
    class VersioningConfiguration:
        def __init__(self, *, MaxVersions: int = ..., Unlimited: bool = ...): ...

class Datastore:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-datastore.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DatastoreName: str = ...,
        DatastoreStorage: "Datastore.DatastoreStorage" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RetentionPeriod: "Datastore.RetentionPeriod" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CustomerManagedS3:
        def __init__(self, *, Bucket: str, RoleArn: str, KeyPrefix: str = ...): ...
    class DatastoreStorage:
        def __init__(
            self,
            *,
            CustomerManagedS3: "Datastore.CustomerManagedS3" = ...,
            ServiceManagedS3: "Datastore.ServiceManagedS3" = ...
        ): ...
    class RetentionPeriod:
        def __init__(self, *, NumberOfDays: int = ..., Unlimited: bool = ...): ...
    class ServiceManagedS3:
        def __init__(self) -> None: ...

class Pipeline:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotanalytics-pipeline.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PipelineActivities: List["Pipeline.Activity"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        PipelineName: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Activity:
        def __init__(
            self,
            *,
            AddAttributes: "Pipeline.AddAttributes" = ...,
            Channel: "Pipeline.Channel" = ...,
            Datastore: "Pipeline.Datastore" = ...,
            DeviceRegistryEnrich: "Pipeline.DeviceRegistryEnrich" = ...,
            DeviceShadowEnrich: "Pipeline.DeviceShadowEnrich" = ...,
            Filter: "Pipeline.Filter" = ...,
            Lambda: "Pipeline.Lambda" = ...,
            Math: "Pipeline.Math" = ...,
            RemoveAttributes: "Pipeline.RemoveAttributes" = ...,
            SelectAttributes: "Pipeline.SelectAttributes" = ...
        ): ...
    class AddAttributes:
        def __init__(
            self, *, Attributes: Any = ..., Name: str = ..., Next: str = ...
        ): ...
    class Channel:
        def __init__(
            self, *, ChannelName: str = ..., Name: str = ..., Next: str = ...
        ): ...
    class Datastore:
        def __init__(self, *, DatastoreName: str = ..., Name: str = ...): ...
    class DeviceRegistryEnrich:
        def __init__(
            self,
            *,
            Attribute: str = ...,
            Name: str = ...,
            Next: str = ...,
            RoleArn: str = ...,
            ThingName: str = ...
        ): ...
    class DeviceShadowEnrich:
        def __init__(
            self,
            *,
            Attribute: str = ...,
            Name: str = ...,
            Next: str = ...,
            RoleArn: str = ...,
            ThingName: str = ...
        ): ...
    class Filter:
        def __init__(self, *, Filter: str = ..., Name: str = ..., Next: str = ...): ...
    class Lambda:
        def __init__(
            self,
            *,
            BatchSize: int = ...,
            LambdaName: str = ...,
            Name: str = ...,
            Next: str = ...
        ): ...
    class Math:
        def __init__(
            self,
            *,
            Attribute: str = ...,
            Math: str = ...,
            Name: str = ...,
            Next: str = ...
        ): ...
    class RemoveAttributes:
        def __init__(
            self, *, Attributes: List[str] = ..., Name: str = ..., Next: str = ...
        ): ...
    class SelectAttributes:
        def __init__(
            self, *, Attributes: List[str] = ..., Name: str = ..., Next: str = ...
        ): ...
