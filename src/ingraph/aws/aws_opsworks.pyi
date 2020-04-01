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

_NAMESPACE = "AWS::OpsWorks"

class App:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-app.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        StackId: str,
        Type: str,
        AppSource: "App.Source" = ...,
        Attributes: Dict[str, str] = ...,
        DataSources: List["App.DataSource"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Domains: List[str] = ...,
        EnableSsl: bool = ...,
        Environment: List["App.EnvironmentVariable"] = ...,
        Shortname: str = ...,
        SslConfiguration: "App.SslConfiguration" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DataSource:
        def __init__(
            self, *, Arn: str = ..., DatabaseName: str = ..., Type: str = ...
        ): ...
    class EnvironmentVariable:
        def __init__(self, *, Key: str, Value: str, Secure: bool = ...): ...
    class Source:
        def __init__(
            self,
            *,
            Password: str = ...,
            Revision: str = ...,
            SshKey: str = ...,
            Type: str = ...,
            Url: str = ...,
            Username: str = ...
        ): ...
    class SslConfiguration:
        def __init__(
            self, *, Certificate: str = ..., Chain: str = ..., PrivateKey: str = ...
        ): ...

class ElasticLoadBalancerAttachment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-elbattachment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ElasticLoadBalancerName: str,
        LayerId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Instance:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-instance.html"""

    AvailabilityZone: Final[str]

    PrivateDnsName: Final[str]

    PrivateIp: Final[str]

    PublicDnsName: Final[str]

    PublicIp: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        InstanceType: str,
        LayerIds: List[str],
        StackId: str,
        AgentVersion: str = ...,
        AmiId: str = ...,
        Architecture: str = ...,
        AutoScalingType: str = ...,
        AvailabilityZone: str = ...,
        BlockDeviceMappings: List["Instance.BlockDeviceMapping"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EbsOptimized: bool = ...,
        ElasticIps: List[str] = ...,
        Hostname: str = ...,
        InstallUpdatesOnBoot: bool = ...,
        Os: str = ...,
        RootDeviceType: str = ...,
        SshKeyName: str = ...,
        SubnetId: str = ...,
        Tenancy: str = ...,
        TimeBasedAutoScaling: "Instance.TimeBasedAutoScaling" = ...,
        UpdateReplacePolicy: str = ...,
        VirtualizationType: str = ...,
        Volumes: List[str] = ...
    ): ...
    class BlockDeviceMapping:
        def __init__(
            self,
            *,
            DeviceName: str = ...,
            Ebs: "Instance.EbsBlockDevice" = ...,
            NoDevice: str = ...,
            VirtualName: str = ...
        ): ...
    class EbsBlockDevice:
        def __init__(
            self,
            *,
            DeleteOnTermination: bool = ...,
            Iops: int = ...,
            SnapshotId: str = ...,
            VolumeSize: int = ...,
            VolumeType: str = ...
        ): ...
    class TimeBasedAutoScaling:
        def __init__(
            self,
            *,
            Friday: Dict[str, str] = ...,
            Monday: Dict[str, str] = ...,
            Saturday: Dict[str, str] = ...,
            Sunday: Dict[str, str] = ...,
            Thursday: Dict[str, str] = ...,
            Tuesday: Dict[str, str] = ...,
            Wednesday: Dict[str, str] = ...
        ): ...

class Layer:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-layer.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AutoAssignElasticIps: bool,
        AutoAssignPublicIps: bool,
        EnableAutoHealing: bool,
        Name: str,
        Shortname: str,
        StackId: str,
        Type: str,
        Attributes: Dict[str, str] = ...,
        CustomInstanceProfileArn: str = ...,
        CustomJson: Any = ...,
        CustomRecipes: "Layer.Recipes" = ...,
        CustomSecurityGroupIds: List[str] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InstallUpdatesOnBoot: bool = ...,
        LifecycleEventConfiguration: "Layer.LifecycleEventConfiguration" = ...,
        LoadBasedAutoScaling: "Layer.LoadBasedAutoScaling" = ...,
        Packages: List[str] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        UseEbsOptimizedInstances: bool = ...,
        VolumeConfigurations: List["Layer.VolumeConfiguration"] = ...
    ): ...
    class AutoScalingThresholds:
        def __init__(
            self,
            *,
            CpuThreshold: float = ...,
            IgnoreMetricsTime: int = ...,
            InstanceCount: int = ...,
            LoadThreshold: float = ...,
            MemoryThreshold: float = ...,
            ThresholdsWaitTime: int = ...
        ): ...
    class LifecycleEventConfiguration:
        def __init__(
            self,
            *,
            ShutdownEventConfiguration: "Layer.ShutdownEventConfiguration" = ...
        ): ...
    class LoadBasedAutoScaling:
        def __init__(
            self,
            *,
            DownScaling: "Layer.AutoScalingThresholds" = ...,
            Enable: bool = ...,
            UpScaling: "Layer.AutoScalingThresholds" = ...
        ): ...
    class Recipes:
        def __init__(
            self,
            *,
            Configure: List[str] = ...,
            Deploy: List[str] = ...,
            Setup: List[str] = ...,
            Shutdown: List[str] = ...,
            Undeploy: List[str] = ...
        ): ...
    class ShutdownEventConfiguration:
        def __init__(
            self,
            *,
            DelayUntilElbConnectionsDrained: bool = ...,
            ExecutionTimeout: int = ...
        ): ...
    class VolumeConfiguration:
        def __init__(
            self,
            *,
            Encrypted: bool = ...,
            Iops: int = ...,
            MountPoint: str = ...,
            NumberOfDisks: int = ...,
            RaidLevel: int = ...,
            Size: int = ...,
            VolumeType: str = ...
        ): ...

class Stack:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-stack.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DefaultInstanceProfileArn: str,
        Name: str,
        ServiceRoleArn: str,
        AgentVersion: str = ...,
        Attributes: Dict[str, str] = ...,
        ChefConfiguration: "Stack.ChefConfiguration" = ...,
        CloneAppIds: List[str] = ...,
        ClonePermissions: bool = ...,
        ConfigurationManager: "Stack.StackConfigurationManager" = ...,
        CustomCookbooksSource: "Stack.Source" = ...,
        CustomJson: Any = ...,
        DefaultAvailabilityZone: str = ...,
        DefaultOs: str = ...,
        DefaultRootDeviceType: str = ...,
        DefaultSshKeyName: str = ...,
        DefaultSubnetId: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EcsClusterArn: str = ...,
        ElasticIps: List["Stack.ElasticIp"] = ...,
        HostnameTheme: str = ...,
        RdsDbInstances: List["Stack.RdsDbInstance"] = ...,
        SourceStackId: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        UseCustomCookbooks: bool = ...,
        UseOpsworksSecurityGroups: bool = ...,
        VpcId: str = ...
    ): ...
    class ChefConfiguration:
        def __init__(
            self, *, BerkshelfVersion: str = ..., ManageBerkshelf: bool = ...
        ): ...
    class ElasticIp:
        def __init__(self, *, Ip: str, Name: str = ...): ...
    class RdsDbInstance:
        def __init__(self, *, DbPassword: str, DbUser: str, RdsDbInstanceArn: str): ...
    class Source:
        def __init__(
            self,
            *,
            Password: str = ...,
            Revision: str = ...,
            SshKey: str = ...,
            Type: str = ...,
            Url: str = ...,
            Username: str = ...
        ): ...
    class StackConfigurationManager:
        def __init__(self, *, Name: str = ..., Version: str = ...): ...

class UserProfile:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-userprofile.html"""

    SshUsername: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        IamUserArn: str,
        AllowSelfManagement: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        SshPublicKey: str = ...,
        SshUsername: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Volume:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworks-volume.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Ec2VolumeId: str,
        StackId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        MountPoint: str = ...,
        Name: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
