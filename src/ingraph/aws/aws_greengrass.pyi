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

_NAMESPACE = "AWS::Greengrass"

class ConnectorDefinition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinition.html"""

    LatestVersionArn: Final[str]

    Id: Final[str]

    Arn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InitialVersion: "ConnectorDefinition.ConnectorDefinitionVersion" = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Connector:
        def __init__(self, *, ConnectorArn: str, Id: str, Parameters: Any = ...): ...
    class ConnectorDefinitionVersion:
        def __init__(self, *, Connectors: List["ConnectorDefinition.Connector"]): ...

class ConnectorDefinitionVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-connectordefinitionversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ConnectorDefinitionId: str,
        Connectors: List["ConnectorDefinitionVersion.Connector"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Connector:
        def __init__(self, *, ConnectorArn: str, Id: str, Parameters: Any = ...): ...

class CoreDefinition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinition.html"""

    LatestVersionArn: Final[str]

    Id: Final[str]

    Arn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InitialVersion: "CoreDefinition.CoreDefinitionVersion" = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Core:
        def __init__(
            self, *, CertificateArn: str, Id: str, ThingArn: str, SyncShadow: bool = ...
        ): ...
    class CoreDefinitionVersion:
        def __init__(self, *, Cores: List["CoreDefinition.Core"]): ...

class CoreDefinitionVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-coredefinitionversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CoreDefinitionId: str,
        Cores: List["CoreDefinitionVersion.Core"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Core:
        def __init__(
            self, *, CertificateArn: str, Id: str, ThingArn: str, SyncShadow: bool = ...
        ): ...

class DeviceDefinition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinition.html"""

    LatestVersionArn: Final[str]

    Id: Final[str]

    Arn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InitialVersion: "DeviceDefinition.DeviceDefinitionVersion" = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Device:
        def __init__(
            self, *, CertificateArn: str, Id: str, ThingArn: str, SyncShadow: bool = ...
        ): ...
    class DeviceDefinitionVersion:
        def __init__(self, *, Devices: List["DeviceDefinition.Device"]): ...

class DeviceDefinitionVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-devicedefinitionversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeviceDefinitionId: str,
        Devices: List["DeviceDefinitionVersion.Device"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Device:
        def __init__(
            self, *, CertificateArn: str, Id: str, ThingArn: str, SyncShadow: bool = ...
        ): ...

class FunctionDefinition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinition.html"""

    LatestVersionArn: Final[str]

    Id: Final[str]

    Arn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InitialVersion: "FunctionDefinition.FunctionDefinitionVersion" = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DefaultConfig:
        def __init__(self, *, Execution: "FunctionDefinition.Execution"): ...
    class Environment:
        def __init__(
            self,
            *,
            AccessSysfs: bool = ...,
            Execution: "FunctionDefinition.Execution" = ...,
            ResourceAccessPolicies: List[
                "FunctionDefinition.ResourceAccessPolicy"
            ] = ...,
            Variables: Any = ...
        ): ...
    class Execution:
        def __init__(
            self, *, IsolationMode: str = ..., RunAs: "FunctionDefinition.RunAs" = ...
        ): ...
    class Function:
        def __init__(
            self,
            *,
            FunctionArn: str,
            FunctionConfiguration: "FunctionDefinition.FunctionConfiguration",
            Id: str
        ): ...
    class FunctionConfiguration:
        def __init__(
            self,
            *,
            EncodingType: str = ...,
            Environment: "FunctionDefinition.Environment" = ...,
            ExecArgs: str = ...,
            Executable: str = ...,
            MemorySize: int = ...,
            Pinned: bool = ...,
            Timeout: int = ...
        ): ...
    class FunctionDefinitionVersion:
        def __init__(
            self,
            *,
            Functions: List["FunctionDefinition.Function"],
            DefaultConfig: "FunctionDefinition.DefaultConfig" = ...
        ): ...
    class ResourceAccessPolicy:
        def __init__(self, *, ResourceId: str, Permission: str = ...): ...
    class RunAs:
        def __init__(self, *, Gid: int = ..., Uid: int = ...): ...

class FunctionDefinitionVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-functiondefinitionversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        FunctionDefinitionId: str,
        Functions: List["FunctionDefinitionVersion.Function"],
        DefaultConfig: "FunctionDefinitionVersion.DefaultConfig" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DefaultConfig:
        def __init__(self, *, Execution: "FunctionDefinitionVersion.Execution"): ...
    class Environment:
        def __init__(
            self,
            *,
            AccessSysfs: bool = ...,
            Execution: "FunctionDefinitionVersion.Execution" = ...,
            ResourceAccessPolicies: List[
                "FunctionDefinitionVersion.ResourceAccessPolicy"
            ] = ...,
            Variables: Any = ...
        ): ...
    class Execution:
        def __init__(
            self,
            *,
            IsolationMode: str = ...,
            RunAs: "FunctionDefinitionVersion.RunAs" = ...
        ): ...
    class Function:
        def __init__(
            self,
            *,
            FunctionArn: str,
            FunctionConfiguration: "FunctionDefinitionVersion.FunctionConfiguration",
            Id: str
        ): ...
    class FunctionConfiguration:
        def __init__(
            self,
            *,
            EncodingType: str = ...,
            Environment: "FunctionDefinitionVersion.Environment" = ...,
            ExecArgs: str = ...,
            Executable: str = ...,
            MemorySize: int = ...,
            Pinned: bool = ...,
            Timeout: int = ...
        ): ...
    class ResourceAccessPolicy:
        def __init__(self, *, ResourceId: str, Permission: str = ...): ...
    class RunAs:
        def __init__(self, *, Gid: int = ..., Uid: int = ...): ...

class Group:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-group.html"""

    RoleAttachedAt: Final[str]

    LatestVersionArn: Final[str]

    Id: Final[str]

    Arn: Final[str]

    RoleArn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InitialVersion: "Group.GroupVersion" = ...,
        RoleArn: str = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class GroupVersion:
        def __init__(
            self,
            *,
            ConnectorDefinitionVersionArn: str = ...,
            CoreDefinitionVersionArn: str = ...,
            DeviceDefinitionVersionArn: str = ...,
            FunctionDefinitionVersionArn: str = ...,
            LoggerDefinitionVersionArn: str = ...,
            ResourceDefinitionVersionArn: str = ...,
            SubscriptionDefinitionVersionArn: str = ...
        ): ...

class GroupVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-groupversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        GroupId: str,
        ConnectorDefinitionVersionArn: str = ...,
        CoreDefinitionVersionArn: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DeviceDefinitionVersionArn: str = ...,
        FunctionDefinitionVersionArn: str = ...,
        LoggerDefinitionVersionArn: str = ...,
        ResourceDefinitionVersionArn: str = ...,
        SubscriptionDefinitionVersionArn: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class LoggerDefinition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinition.html"""

    LatestVersionArn: Final[str]

    Id: Final[str]

    Arn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InitialVersion: "LoggerDefinition.LoggerDefinitionVersion" = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Logger:
        def __init__(
            self, *, Component: str, Id: str, Level: str, Type: str, Space: int = ...
        ): ...
    class LoggerDefinitionVersion:
        def __init__(self, *, Loggers: List["LoggerDefinition.Logger"]): ...

class LoggerDefinitionVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-loggerdefinitionversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        LoggerDefinitionId: str,
        Loggers: List["LoggerDefinitionVersion.Logger"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Logger:
        def __init__(
            self, *, Component: str, Id: str, Level: str, Type: str, Space: int = ...
        ): ...

class ResourceDefinition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinition.html"""

    LatestVersionArn: Final[str]

    Id: Final[str]

    Arn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InitialVersion: "ResourceDefinition.ResourceDefinitionVersion" = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class GroupOwnerSetting:
        def __init__(self, *, AutoAddGroupOwner: bool, GroupOwner: str = ...): ...
    class LocalDeviceResourceData:
        def __init__(
            self,
            *,
            SourcePath: str,
            GroupOwnerSetting: "ResourceDefinition.GroupOwnerSetting" = ...
        ): ...
    class LocalVolumeResourceData:
        def __init__(
            self,
            *,
            DestinationPath: str,
            SourcePath: str,
            GroupOwnerSetting: "ResourceDefinition.GroupOwnerSetting" = ...
        ): ...
    class ResourceDataContainer:
        def __init__(
            self,
            *,
            LocalDeviceResourceData: "ResourceDefinition.LocalDeviceResourceData" = ...,
            LocalVolumeResourceData: "ResourceDefinition.LocalVolumeResourceData" = ...,
            S3MachineLearningModelResourceData: "ResourceDefinition.S3MachineLearningModelResourceData" = ...,
            SageMakerMachineLearningModelResourceData: "ResourceDefinition.SageMakerMachineLearningModelResourceData" = ...,
            SecretsManagerSecretResourceData: "ResourceDefinition.SecretsManagerSecretResourceData" = ...
        ): ...
    class ResourceDefinitionVersion:
        def __init__(
            self, *, Resources: List["ResourceDefinition.ResourceInstance"]
        ): ...
    class ResourceDownloadOwnerSetting:
        def __init__(self, *, GroupOwner: str, GroupPermission: str): ...
    class ResourceInstance:
        def __init__(
            self,
            *,
            Id: str,
            Name: str,
            ResourceDataContainer: "ResourceDefinition.ResourceDataContainer"
        ): ...
    class S3MachineLearningModelResourceData:
        def __init__(
            self,
            *,
            DestinationPath: str,
            S3Uri: str,
            OwnerSetting: "ResourceDefinition.ResourceDownloadOwnerSetting" = ...
        ): ...
    class SageMakerMachineLearningModelResourceData:
        def __init__(
            self,
            *,
            DestinationPath: str,
            SageMakerJobArn: str,
            OwnerSetting: "ResourceDefinition.ResourceDownloadOwnerSetting" = ...
        ): ...
    class SecretsManagerSecretResourceData:
        def __init__(
            self, *, ARN: str, AdditionalStagingLabelsToDownload: List[str] = ...
        ): ...

class ResourceDefinitionVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-resourcedefinitionversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ResourceDefinitionId: str,
        Resources: List["ResourceDefinitionVersion.ResourceInstance"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class GroupOwnerSetting:
        def __init__(self, *, AutoAddGroupOwner: bool, GroupOwner: str = ...): ...
    class LocalDeviceResourceData:
        def __init__(
            self,
            *,
            SourcePath: str,
            GroupOwnerSetting: "ResourceDefinitionVersion.GroupOwnerSetting" = ...
        ): ...
    class LocalVolumeResourceData:
        def __init__(
            self,
            *,
            DestinationPath: str,
            SourcePath: str,
            GroupOwnerSetting: "ResourceDefinitionVersion.GroupOwnerSetting" = ...
        ): ...
    class ResourceDataContainer:
        def __init__(
            self,
            *,
            LocalDeviceResourceData: "ResourceDefinitionVersion.LocalDeviceResourceData" = ...,
            LocalVolumeResourceData: "ResourceDefinitionVersion.LocalVolumeResourceData" = ...,
            S3MachineLearningModelResourceData: "ResourceDefinitionVersion.S3MachineLearningModelResourceData" = ...,
            SageMakerMachineLearningModelResourceData: "ResourceDefinitionVersion.SageMakerMachineLearningModelResourceData" = ...,
            SecretsManagerSecretResourceData: "ResourceDefinitionVersion.SecretsManagerSecretResourceData" = ...
        ): ...
    class ResourceDownloadOwnerSetting:
        def __init__(self, *, GroupOwner: str, GroupPermission: str): ...
    class ResourceInstance:
        def __init__(
            self,
            *,
            Id: str,
            Name: str,
            ResourceDataContainer: "ResourceDefinitionVersion.ResourceDataContainer"
        ): ...
    class S3MachineLearningModelResourceData:
        def __init__(
            self,
            *,
            DestinationPath: str,
            S3Uri: str,
            OwnerSetting: "ResourceDefinitionVersion.ResourceDownloadOwnerSetting" = ...
        ): ...
    class SageMakerMachineLearningModelResourceData:
        def __init__(
            self,
            *,
            DestinationPath: str,
            SageMakerJobArn: str,
            OwnerSetting: "ResourceDefinitionVersion.ResourceDownloadOwnerSetting" = ...
        ): ...
    class SecretsManagerSecretResourceData:
        def __init__(
            self, *, ARN: str, AdditionalStagingLabelsToDownload: List[str] = ...
        ): ...

class SubscriptionDefinition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinition.html"""

    LatestVersionArn: Final[str]

    Id: Final[str]

    Arn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InitialVersion: "SubscriptionDefinition.SubscriptionDefinitionVersion" = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Subscription:
        def __init__(self, *, Id: str, Source: str, Subject: str, Target: str): ...
    class SubscriptionDefinitionVersion:
        def __init__(
            self, *, Subscriptions: List["SubscriptionDefinition.Subscription"]
        ): ...

class SubscriptionDefinitionVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-greengrass-subscriptiondefinitionversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        SubscriptionDefinitionId: str,
        Subscriptions: List["SubscriptionDefinitionVersion.Subscription"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Subscription:
        def __init__(self, *, Id: str, Source: str, Subject: str, Target: str): ...
