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

_NAMESPACE = "AWS::EMR"

class Cluster:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-cluster.html"""

    MasterPublicDNS: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Instances: "Cluster.JobFlowInstancesConfig",
        JobFlowRole: str,
        Name: str,
        ServiceRole: str,
        AdditionalInfo: Any = ...,
        Applications: List["Cluster.Application"] = ...,
        AutoScalingRole: str = ...,
        BootstrapActions: List["Cluster.BootstrapActionConfig"] = ...,
        Configurations: List["Cluster.Configuration"] = ...,
        CustomAmiId: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EbsRootVolumeSize: int = ...,
        KerberosAttributes: "Cluster.KerberosAttributes" = ...,
        LogUri: str = ...,
        ReleaseLabel: str = ...,
        ScaleDownBehavior: str = ...,
        SecurityConfiguration: str = ...,
        Steps: List["Cluster.StepConfig"] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VisibleToAllUsers: bool = ...
    ): ...
    class Application:
        def __init__(
            self,
            *,
            AdditionalInfo: Dict[str, str] = ...,
            Args: List[str] = ...,
            Name: str = ...,
            Version: str = ...
        ): ...
    class AutoScalingPolicy:
        def __init__(
            self,
            *,
            Constraints: "Cluster.ScalingConstraints",
            Rules: List["Cluster.ScalingRule"]
        ): ...
    class BootstrapActionConfig:
        def __init__(
            self,
            *,
            Name: str,
            ScriptBootstrapAction: "Cluster.ScriptBootstrapActionConfig"
        ): ...
    class CloudWatchAlarmDefinition:
        def __init__(
            self,
            *,
            ComparisonOperator: str,
            MetricName: str,
            Period: int,
            Threshold: float,
            Dimensions: List["Cluster.MetricDimension"] = ...,
            EvaluationPeriods: int = ...,
            Namespace: str = ...,
            Statistic: str = ...,
            Unit: str = ...
        ): ...
    class Configuration:
        def __init__(
            self,
            *,
            Classification: str = ...,
            ConfigurationProperties: Dict[str, str] = ...,
            Configurations: List["Cluster.Configuration"] = ...
        ): ...
    class EbsBlockDeviceConfig:
        def __init__(
            self,
            *,
            VolumeSpecification: "Cluster.VolumeSpecification",
            VolumesPerInstance: int = ...
        ): ...
    class EbsConfiguration:
        def __init__(
            self,
            *,
            EbsBlockDeviceConfigs: List["Cluster.EbsBlockDeviceConfig"] = ...,
            EbsOptimized: bool = ...
        ): ...
    class HadoopJarStepConfig:
        def __init__(
            self,
            *,
            Jar: str,
            Args: List[str] = ...,
            MainClass: str = ...,
            StepProperties: List["Cluster.KeyValue"] = ...
        ): ...
    class InstanceFleetConfig:
        def __init__(
            self,
            *,
            InstanceTypeConfigs: List["Cluster.InstanceTypeConfig"] = ...,
            LaunchSpecifications: "Cluster.InstanceFleetProvisioningSpecifications" = ...,
            Name: str = ...,
            TargetOnDemandCapacity: int = ...,
            TargetSpotCapacity: int = ...
        ): ...
    class InstanceFleetProvisioningSpecifications:
        def __init__(
            self, *, SpotSpecification: "Cluster.SpotProvisioningSpecification"
        ): ...
    class InstanceGroupConfig:
        def __init__(
            self,
            *,
            InstanceCount: int,
            InstanceType: str,
            AutoScalingPolicy: "Cluster.AutoScalingPolicy" = ...,
            BidPrice: str = ...,
            Configurations: List["Cluster.Configuration"] = ...,
            EbsConfiguration: "Cluster.EbsConfiguration" = ...,
            Market: str = ...,
            Name: str = ...
        ): ...
    class InstanceTypeConfig:
        def __init__(
            self,
            *,
            InstanceType: str,
            BidPrice: str = ...,
            BidPriceAsPercentageOfOnDemandPrice: float = ...,
            Configurations: List["Cluster.Configuration"] = ...,
            EbsConfiguration: "Cluster.EbsConfiguration" = ...,
            WeightedCapacity: int = ...
        ): ...
    class JobFlowInstancesConfig:
        def __init__(
            self,
            *,
            AdditionalMasterSecurityGroups: List[str] = ...,
            AdditionalSlaveSecurityGroups: List[str] = ...,
            CoreInstanceFleet: "Cluster.InstanceFleetConfig" = ...,
            CoreInstanceGroup: "Cluster.InstanceGroupConfig" = ...,
            Ec2KeyName: str = ...,
            Ec2SubnetId: str = ...,
            Ec2SubnetIds: List[str] = ...,
            EmrManagedMasterSecurityGroup: str = ...,
            EmrManagedSlaveSecurityGroup: str = ...,
            HadoopVersion: str = ...,
            KeepJobFlowAliveWhenNoSteps: bool = ...,
            MasterInstanceFleet: "Cluster.InstanceFleetConfig" = ...,
            MasterInstanceGroup: "Cluster.InstanceGroupConfig" = ...,
            Placement: "Cluster.PlacementType" = ...,
            ServiceAccessSecurityGroup: str = ...,
            TerminationProtected: bool = ...
        ): ...
    class KerberosAttributes:
        def __init__(
            self,
            *,
            KdcAdminPassword: str,
            Realm: str,
            ADDomainJoinPassword: str = ...,
            ADDomainJoinUser: str = ...,
            CrossRealmTrustPrincipalPassword: str = ...
        ): ...
    class KeyValue:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...
    class MetricDimension:
        def __init__(self, *, Key: str, Value: str): ...
    class PlacementType:
        def __init__(self, *, AvailabilityZone: str): ...
    class ScalingAction:
        def __init__(
            self,
            *,
            SimpleScalingPolicyConfiguration: "Cluster.SimpleScalingPolicyConfiguration",
            Market: str = ...
        ): ...
    class ScalingConstraints:
        def __init__(self, *, MaxCapacity: int, MinCapacity: int): ...
    class ScalingRule:
        def __init__(
            self,
            *,
            Action: "Cluster.ScalingAction",
            Name: str,
            Trigger: "Cluster.ScalingTrigger",
            Description: str = ...
        ): ...
    class ScalingTrigger:
        def __init__(
            self, *, CloudWatchAlarmDefinition: "Cluster.CloudWatchAlarmDefinition"
        ): ...
    class ScriptBootstrapActionConfig:
        def __init__(self, *, Path: str, Args: List[str] = ...): ...
    class SimpleScalingPolicyConfiguration:
        def __init__(
            self,
            *,
            ScalingAdjustment: int,
            AdjustmentType: str = ...,
            CoolDown: int = ...
        ): ...
    class SpotProvisioningSpecification:
        def __init__(
            self,
            *,
            TimeoutAction: str,
            TimeoutDurationMinutes: int,
            BlockDurationMinutes: int = ...
        ): ...
    class StepConfig:
        def __init__(
            self,
            *,
            HadoopJarStep: "Cluster.HadoopJarStepConfig",
            Name: str,
            ActionOnFailure: str = ...
        ): ...
    class VolumeSpecification:
        def __init__(self, *, SizeInGB: int, VolumeType: str, Iops: int = ...): ...

class InstanceFleetConfig:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticmapreduce-instancefleetconfig.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ClusterId: str,
        InstanceFleetType: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InstanceTypeConfigs: List["InstanceFleetConfig.InstanceTypeConfig"] = ...,
        LaunchSpecifications: "InstanceFleetConfig.InstanceFleetProvisioningSpecifications" = ...,
        Name: str = ...,
        TargetOnDemandCapacity: int = ...,
        TargetSpotCapacity: int = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Configuration:
        def __init__(
            self,
            *,
            Classification: str = ...,
            ConfigurationProperties: Dict[str, str] = ...,
            Configurations: List["InstanceFleetConfig.Configuration"] = ...
        ): ...
    class EbsBlockDeviceConfig:
        def __init__(
            self,
            *,
            VolumeSpecification: "InstanceFleetConfig.VolumeSpecification",
            VolumesPerInstance: int = ...
        ): ...
    class EbsConfiguration:
        def __init__(
            self,
            *,
            EbsBlockDeviceConfigs: List[
                "InstanceFleetConfig.EbsBlockDeviceConfig"
            ] = ...,
            EbsOptimized: bool = ...
        ): ...
    class InstanceFleetProvisioningSpecifications:
        def __init__(
            self,
            *,
            SpotSpecification: "InstanceFleetConfig.SpotProvisioningSpecification"
        ): ...
    class InstanceTypeConfig:
        def __init__(
            self,
            *,
            InstanceType: str,
            BidPrice: str = ...,
            BidPriceAsPercentageOfOnDemandPrice: float = ...,
            Configurations: List["InstanceFleetConfig.Configuration"] = ...,
            EbsConfiguration: "InstanceFleetConfig.EbsConfiguration" = ...,
            WeightedCapacity: int = ...
        ): ...
    class SpotProvisioningSpecification:
        def __init__(
            self,
            *,
            TimeoutAction: str,
            TimeoutDurationMinutes: int,
            BlockDurationMinutes: int = ...
        ): ...
    class VolumeSpecification:
        def __init__(self, *, SizeInGB: int, VolumeType: str, Iops: int = ...): ...

class InstanceGroupConfig:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-instancegroupconfig.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        InstanceCount: int,
        InstanceRole: str,
        InstanceType: str,
        JobFlowId: str,
        AutoScalingPolicy: "InstanceGroupConfig.AutoScalingPolicy" = ...,
        BidPrice: str = ...,
        Configurations: List["InstanceGroupConfig.Configuration"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EbsConfiguration: "InstanceGroupConfig.EbsConfiguration" = ...,
        Market: str = ...,
        Name: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AutoScalingPolicy:
        def __init__(
            self,
            *,
            Constraints: "InstanceGroupConfig.ScalingConstraints",
            Rules: List["InstanceGroupConfig.ScalingRule"]
        ): ...
    class CloudWatchAlarmDefinition:
        def __init__(
            self,
            *,
            ComparisonOperator: str,
            MetricName: str,
            Period: int,
            Threshold: float,
            Dimensions: List["InstanceGroupConfig.MetricDimension"] = ...,
            EvaluationPeriods: int = ...,
            Namespace: str = ...,
            Statistic: str = ...,
            Unit: str = ...
        ): ...
    class Configuration:
        def __init__(
            self,
            *,
            Classification: str = ...,
            ConfigurationProperties: Dict[str, str] = ...,
            Configurations: List["InstanceGroupConfig.Configuration"] = ...
        ): ...
    class EbsBlockDeviceConfig:
        def __init__(
            self,
            *,
            VolumeSpecification: "InstanceGroupConfig.VolumeSpecification",
            VolumesPerInstance: int = ...
        ): ...
    class EbsConfiguration:
        def __init__(
            self,
            *,
            EbsBlockDeviceConfigs: List[
                "InstanceGroupConfig.EbsBlockDeviceConfig"
            ] = ...,
            EbsOptimized: bool = ...
        ): ...
    class MetricDimension:
        def __init__(self, *, Key: str, Value: str): ...
    class ScalingAction:
        def __init__(
            self,
            *,
            SimpleScalingPolicyConfiguration: "InstanceGroupConfig.SimpleScalingPolicyConfiguration",
            Market: str = ...
        ): ...
    class ScalingConstraints:
        def __init__(self, *, MaxCapacity: int, MinCapacity: int): ...
    class ScalingRule:
        def __init__(
            self,
            *,
            Action: "InstanceGroupConfig.ScalingAction",
            Name: str,
            Trigger: "InstanceGroupConfig.ScalingTrigger",
            Description: str = ...
        ): ...
    class ScalingTrigger:
        def __init__(
            self,
            *,
            CloudWatchAlarmDefinition: "InstanceGroupConfig.CloudWatchAlarmDefinition"
        ): ...
    class SimpleScalingPolicyConfiguration:
        def __init__(
            self,
            *,
            ScalingAdjustment: int,
            AdjustmentType: str = ...,
            CoolDown: int = ...
        ): ...
    class VolumeSpecification:
        def __init__(self, *, SizeInGB: int, VolumeType: str, Iops: int = ...): ...

class SecurityConfiguration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-securityconfiguration.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        SecurityConfiguration: Any,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Step:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emr-step.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ActionOnFailure: str,
        HadoopJarStep: "Step.HadoopJarStepConfig",
        JobFlowId: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class HadoopJarStepConfig:
        def __init__(
            self,
            *,
            Jar: str,
            Args: List[str] = ...,
            MainClass: str = ...,
            StepProperties: List["Step.KeyValue"] = ...
        ): ...
    class KeyValue:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...
