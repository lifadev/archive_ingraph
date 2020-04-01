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

_NAMESPACE = "AWS::ECS"

class Cluster:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-cluster.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ClusterName: str = ...,
        ClusterSettings: List["Cluster.ClusterSetting"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ClusterSetting:
        def __init__(self, *, Name: str, Value: str): ...

class PrimaryTaskSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-primarytaskset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Cluster: str,
        Service: str,
        TaskSetId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Service:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html"""

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Cluster: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DeploymentConfiguration: "Service.DeploymentConfiguration" = ...,
        DeploymentController: "Service.DeploymentController" = ...,
        DesiredCount: int = ...,
        EnableECSManagedTags: bool = ...,
        HealthCheckGracePeriodSeconds: int = ...,
        LaunchType: str = ...,
        LoadBalancers: List["Service.LoadBalancer"] = ...,
        NetworkConfiguration: "Service.NetworkConfiguration" = ...,
        PlacementConstraints: List["Service.PlacementConstraint"] = ...,
        PlacementStrategies: List["Service.PlacementStrategy"] = ...,
        PlatformVersion: str = ...,
        PropagateTags: str = ...,
        Role: str = ...,
        SchedulingStrategy: str = ...,
        ServiceName: str = ...,
        ServiceRegistries: List["Service.ServiceRegistry"] = ...,
        Tags: List["Tag"] = ...,
        TaskDefinition: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AwsVpcConfiguration:
        def __init__(
            self,
            *,
            Subnets: List[str],
            AssignPublicIp: str = ...,
            SecurityGroups: List[str] = ...
        ): ...
    class DeploymentConfiguration:
        def __init__(
            self, *, MaximumPercent: int = ..., MinimumHealthyPercent: int = ...
        ): ...
    class DeploymentController:
        def __init__(self, *, Type: str = ...): ...
    class LoadBalancer:
        def __init__(
            self,
            *,
            ContainerPort: int,
            ContainerName: str = ...,
            LoadBalancerName: str = ...,
            TargetGroupArn: str = ...
        ): ...
    class NetworkConfiguration:
        def __init__(
            self, *, AwsvpcConfiguration: "Service.AwsVpcConfiguration" = ...
        ): ...
    class PlacementConstraint:
        def __init__(self, *, Type: str, Expression: str = ...): ...
    class PlacementStrategy:
        def __init__(self, *, Type: str, Field: str = ...): ...
    class ServiceRegistry:
        def __init__(
            self,
            *,
            ContainerName: str = ...,
            ContainerPort: int = ...,
            Port: int = ...,
            RegistryArn: str = ...
        ): ...

class TaskDefinition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskdefinition.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ContainerDefinitions: List["TaskDefinition.ContainerDefinition"] = ...,
        Cpu: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ExecutionRoleArn: str = ...,
        Family: str = ...,
        InferenceAccelerators: List["TaskDefinition.InferenceAccelerator"] = ...,
        IpcMode: str = ...,
        Memory: str = ...,
        NetworkMode: str = ...,
        PidMode: str = ...,
        PlacementConstraints: List[
            "TaskDefinition.TaskDefinitionPlacementConstraint"
        ] = ...,
        ProxyConfiguration: "TaskDefinition.ProxyConfiguration" = ...,
        RequiresCompatibilities: List[str] = ...,
        Tags: List["Tag"] = ...,
        TaskRoleArn: str = ...,
        UpdateReplacePolicy: str = ...,
        Volumes: List["TaskDefinition.Volume"] = ...
    ): ...
    class ContainerDefinition:
        def __init__(
            self,
            *,
            Command: List[str] = ...,
            Cpu: int = ...,
            DependsOn: List["TaskDefinition.ContainerDependency"] = ...,
            DisableNetworking: bool = ...,
            DnsSearchDomains: List[str] = ...,
            DnsServers: List[str] = ...,
            DockerLabels: Dict[str, str] = ...,
            DockerSecurityOptions: List[str] = ...,
            EntryPoint: List[str] = ...,
            Environment: List["TaskDefinition.KeyValuePair"] = ...,
            Essential: bool = ...,
            ExtraHosts: List["TaskDefinition.HostEntry"] = ...,
            FirelensConfiguration: "TaskDefinition.FirelensConfiguration" = ...,
            HealthCheck: "TaskDefinition.HealthCheck" = ...,
            Hostname: str = ...,
            Image: str = ...,
            Interactive: bool = ...,
            Links: List[str] = ...,
            LinuxParameters: "TaskDefinition.LinuxParameters" = ...,
            LogConfiguration: "TaskDefinition.LogConfiguration" = ...,
            Memory: int = ...,
            MemoryReservation: int = ...,
            MountPoints: List["TaskDefinition.MountPoint"] = ...,
            Name: str = ...,
            PortMappings: List["TaskDefinition.PortMapping"] = ...,
            Privileged: bool = ...,
            PseudoTerminal: bool = ...,
            ReadonlyRootFilesystem: bool = ...,
            RepositoryCredentials: "TaskDefinition.RepositoryCredentials" = ...,
            ResourceRequirements: List["TaskDefinition.ResourceRequirement"] = ...,
            Secrets: List["TaskDefinition.Secret"] = ...,
            StartTimeout: int = ...,
            StopTimeout: int = ...,
            SystemControls: List["TaskDefinition.SystemControl"] = ...,
            Ulimits: List["TaskDefinition.Ulimit"] = ...,
            User: str = ...,
            VolumesFrom: List["TaskDefinition.VolumeFrom"] = ...,
            WorkingDirectory: str = ...
        ): ...
    class ContainerDependency:
        def __init__(self, *, Condition: str, ContainerName: str): ...
    class Device:
        def __init__(
            self,
            *,
            HostPath: str,
            ContainerPath: str = ...,
            Permissions: List[str] = ...
        ): ...
    class DockerVolumeConfiguration:
        def __init__(
            self,
            *,
            Autoprovision: bool = ...,
            Driver: str = ...,
            DriverOpts: Dict[str, str] = ...,
            Labels: Dict[str, str] = ...,
            Scope: str = ...
        ): ...
    class FirelensConfiguration:
        def __init__(self, *, Type: str, Options: Dict[str, str] = ...): ...
    class HealthCheck:
        def __init__(
            self,
            *,
            Command: List[str],
            Interval: int = ...,
            Retries: int = ...,
            StartPeriod: int = ...,
            Timeout: int = ...
        ): ...
    class HostEntry:
        def __init__(self, *, Hostname: str, IpAddress: str): ...
    class HostVolumeProperties:
        def __init__(self, *, SourcePath: str = ...): ...
    class InferenceAccelerator:
        def __init__(
            self,
            *,
            DeviceName: str = ...,
            DevicePolicy: str = ...,
            DeviceType: str = ...
        ): ...
    class KernelCapabilities:
        def __init__(self, *, Add: List[str] = ..., Drop: List[str] = ...): ...
    class KeyValuePair:
        def __init__(self, *, Name: str = ..., Value: str = ...): ...
    class LinuxParameters:
        def __init__(
            self,
            *,
            Capabilities: "TaskDefinition.KernelCapabilities" = ...,
            Devices: List["TaskDefinition.Device"] = ...,
            InitProcessEnabled: bool = ...,
            MaxSwap: int = ...,
            SharedMemorySize: int = ...,
            Swappiness: int = ...,
            Tmpfs: List["TaskDefinition.Tmpfs"] = ...
        ): ...
    class LogConfiguration:
        def __init__(
            self,
            *,
            LogDriver: str,
            Options: Dict[str, str] = ...,
            SecretOptions: List["TaskDefinition.Secret"] = ...
        ): ...
    class MountPoint:
        def __init__(
            self,
            *,
            ContainerPath: str = ...,
            ReadOnly: bool = ...,
            SourceVolume: str = ...
        ): ...
    class PortMapping:
        def __init__(
            self, *, ContainerPort: int = ..., HostPort: int = ..., Protocol: str = ...
        ): ...
    class ProxyConfiguration:
        def __init__(
            self,
            *,
            ContainerName: str,
            ProxyConfigurationProperties: List["TaskDefinition.KeyValuePair"] = ...,
            Type: str = ...
        ): ...
    class RepositoryCredentials:
        def __init__(self, *, CredentialsParameter: str = ...): ...
    class ResourceRequirement:
        def __init__(self, *, Type: str, Value: str): ...
    class Secret:
        def __init__(self, *, Name: str, ValueFrom: str): ...
    class SystemControl:
        def __init__(self, *, Namespace: str, Value: str): ...
    class TaskDefinitionPlacementConstraint:
        def __init__(self, *, Type: str, Expression: str = ...): ...
    class Tmpfs:
        def __init__(
            self, *, Size: int, ContainerPath: str = ..., MountOptions: List[str] = ...
        ): ...
    class Ulimit:
        def __init__(self, *, HardLimit: int, Name: str, SoftLimit: int): ...
    class Volume:
        def __init__(
            self,
            *,
            DockerVolumeConfiguration: "TaskDefinition.DockerVolumeConfiguration" = ...,
            Host: "TaskDefinition.HostVolumeProperties" = ...,
            Name: str = ...
        ): ...
    class VolumeFrom:
        def __init__(self, *, ReadOnly: bool = ..., SourceContainer: str = ...): ...

class TaskSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-taskset.html"""

    Id: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Cluster: str,
        Service: str,
        TaskDefinition: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ExternalId: str = ...,
        LaunchType: str = ...,
        LoadBalancers: List["TaskSet.LoadBalancer"] = ...,
        NetworkConfiguration: "TaskSet.NetworkConfiguration" = ...,
        PlatformVersion: str = ...,
        Scale: "TaskSet.Scale" = ...,
        ServiceRegistries: List["TaskSet.ServiceRegistry"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AwsVpcConfiguration:
        def __init__(
            self,
            *,
            Subnets: List[str],
            AssignPublicIp: str = ...,
            SecurityGroups: List[str] = ...
        ): ...
    class LoadBalancer:
        def __init__(
            self,
            *,
            ContainerName: str = ...,
            ContainerPort: int = ...,
            LoadBalancerName: str = ...,
            TargetGroupArn: str = ...
        ): ...
    class NetworkConfiguration:
        def __init__(
            self, *, AwsVpcConfiguration: "TaskSet.AwsVpcConfiguration" = ...
        ): ...
    class Scale:
        def __init__(self, *, Unit: str = ..., Value: float = ...): ...
    class ServiceRegistry:
        def __init__(
            self,
            *,
            ContainerName: str = ...,
            ContainerPort: int = ...,
            Port: int = ...,
            RegistryArn: str = ...
        ): ...
