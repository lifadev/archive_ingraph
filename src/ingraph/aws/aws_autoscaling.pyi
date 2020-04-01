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

_NAMESPACE = "AWS::AutoScaling"

class AutoScalingGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-group.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        MaxSize: str,
        MinSize: str,
        AutoScalingGroupName: str = ...,
        AvailabilityZones: List[str] = ...,
        Cooldown: str = ...,
        CreationPolicy: "AutoScalingGroup.CreationPolicy" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DesiredCapacity: str = ...,
        HealthCheckGracePeriod: int = ...,
        HealthCheckType: str = ...,
        InstanceId: str = ...,
        LaunchConfigurationName: str = ...,
        LaunchTemplate: "AutoScalingGroup.LaunchTemplateSpecification" = ...,
        LifecycleHookSpecificationList: List[
            "AutoScalingGroup.LifecycleHookSpecification"
        ] = ...,
        LoadBalancerNames: List[str] = ...,
        MaxInstanceLifetime: int = ...,
        MetricsCollection: List["AutoScalingGroup.MetricsCollection"] = ...,
        MixedInstancesPolicy: "AutoScalingGroup.MixedInstancesPolicy" = ...,
        NotificationConfigurations: List[
            "AutoScalingGroup.NotificationConfiguration"
        ] = ...,
        PlacementGroup: str = ...,
        ServiceLinkedRoleARN: str = ...,
        Tags: List["AutoScalingGroup.TagProperty"] = ...,
        TargetGroupARNs: List[str] = ...,
        TerminationPolicies: List[str] = ...,
        UpdatePolicy: "AutoScalingGroup.UpdatePolicy" = ...,
        UpdateReplacePolicy: str = ...,
        VPCZoneIdentifier: List[str] = ...
    ): ...
    class AutoScalingCreationPolicy:
        def __init__(self, *, MinSuccessfulInstancesPercent: int = ...): ...
    class AutoScalingReplacingUpdate:
        def __init__(self, *, WillReplace: bool = ...): ...
    class AutoScalingRollingUpdate:
        def __init__(
            self,
            *,
            MaxBatchSize: int = ...,
            MinInstancesInService: int = ...,
            MinSuccessfulInstancesPercent: int = ...,
            PauseTime: str = ...,
            SuspendProcesses: List[str] = ...,
            WaitOnResourceSignals: bool = ...
        ): ...
    class AutoScalingScheduledAction:
        def __init__(self, *, IgnoreUnmodifiedGroupSizeProperties: bool = ...): ...
    class CreationPolicy:
        def __init__(
            self,
            *,
            AutoScalingCreationPolicy: "AutoScalingGroup.AutoScalingCreationPolicy" = ...,
            ResourceSignal: "AutoScalingGroup.ResourceSignal" = ...
        ): ...
    class InstancesDistribution:
        def __init__(
            self,
            *,
            OnDemandAllocationStrategy: str = ...,
            OnDemandBaseCapacity: int = ...,
            OnDemandPercentageAboveBaseCapacity: int = ...,
            SpotAllocationStrategy: str = ...,
            SpotInstancePools: int = ...,
            SpotMaxPrice: str = ...
        ): ...
    class LaunchTemplate:
        def __init__(
            self,
            *,
            LaunchTemplateSpecification: "AutoScalingGroup.LaunchTemplateSpecification",
            Overrides: List["AutoScalingGroup.LaunchTemplateOverrides"] = ...
        ): ...
    class LaunchTemplateOverrides:
        def __init__(self, *, InstanceType: str = ..., WeightedCapacity: str = ...): ...
    class LaunchTemplateSpecification:
        def __init__(
            self,
            *,
            Version: str,
            LaunchTemplateId: str = ...,
            LaunchTemplateName: str = ...
        ): ...
    class LifecycleHookSpecification:
        def __init__(
            self,
            *,
            LifecycleHookName: str,
            LifecycleTransition: str,
            DefaultResult: str = ...,
            HeartbeatTimeout: int = ...,
            NotificationMetadata: str = ...,
            NotificationTargetARN: str = ...,
            RoleARN: str = ...
        ): ...
    class MetricsCollection:
        def __init__(self, *, Granularity: str, Metrics: List[str] = ...): ...
    class MixedInstancesPolicy:
        def __init__(
            self,
            *,
            LaunchTemplate: "AutoScalingGroup.LaunchTemplate",
            InstancesDistribution: "AutoScalingGroup.InstancesDistribution" = ...
        ): ...
    class NotificationConfiguration:
        def __init__(self, *, TopicARN: str, NotificationTypes: List[str] = ...): ...
    class ResourceSignal:
        def __init__(self, *, Count: int = ..., Timeout: str = ...): ...
    class TagProperty:
        def __init__(self, *, Key: str, PropagateAtLaunch: bool, Value: str): ...
    class UpdatePolicy:
        def __init__(
            self,
            *,
            AutoScalingReplacingUpdate: "AutoScalingGroup.AutoScalingReplacingUpdate" = ...,
            AutoScalingRollingUpdate: "AutoScalingGroup.AutoScalingRollingUpdate" = ...,
            AutoScalingScheduledAction: "AutoScalingGroup.AutoScalingScheduledAction" = ...
        ): ...

class LaunchConfiguration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-launchconfig.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ImageId: str,
        InstanceType: str,
        AssociatePublicIpAddress: bool = ...,
        BlockDeviceMappings: List["LaunchConfiguration.BlockDeviceMapping"] = ...,
        ClassicLinkVPCId: str = ...,
        ClassicLinkVPCSecurityGroups: List[str] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EbsOptimized: bool = ...,
        IamInstanceProfile: str = ...,
        InstanceId: str = ...,
        InstanceMonitoring: bool = ...,
        KernelId: str = ...,
        KeyName: str = ...,
        LaunchConfigurationName: str = ...,
        PlacementTenancy: str = ...,
        RamDiskId: str = ...,
        SecurityGroups: List[str] = ...,
        SpotPrice: str = ...,
        UpdateReplacePolicy: str = ...,
        UserData: str = ...
    ): ...
    class BlockDevice:
        def __init__(
            self,
            *,
            DeleteOnTermination: bool = ...,
            Encrypted: bool = ...,
            Iops: int = ...,
            SnapshotId: str = ...,
            VolumeSize: int = ...,
            VolumeType: str = ...
        ): ...
    class BlockDeviceMapping:
        def __init__(
            self,
            *,
            DeviceName: str,
            Ebs: "LaunchConfiguration.BlockDevice" = ...,
            NoDevice: bool = ...,
            VirtualName: str = ...
        ): ...

class LifecycleHook:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-lifecyclehook.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AutoScalingGroupName: str,
        LifecycleTransition: str,
        DefaultResult: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        HeartbeatTimeout: int = ...,
        LifecycleHookName: str = ...,
        NotificationMetadata: str = ...,
        NotificationTargetARN: str = ...,
        RoleARN: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ScalingPolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-as-policy.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AutoScalingGroupName: str,
        AdjustmentType: str = ...,
        Cooldown: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EstimatedInstanceWarmup: int = ...,
        MetricAggregationType: str = ...,
        MinAdjustmentMagnitude: int = ...,
        PolicyType: str = ...,
        ScalingAdjustment: int = ...,
        StepAdjustments: List["ScalingPolicy.StepAdjustment"] = ...,
        TargetTrackingConfiguration: "ScalingPolicy.TargetTrackingConfiguration" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CustomizedMetricSpecification:
        def __init__(
            self,
            *,
            MetricName: str,
            Namespace: str,
            Statistic: str,
            Dimensions: List["ScalingPolicy.MetricDimension"] = ...,
            Unit: str = ...
        ): ...
    class MetricDimension:
        def __init__(self, *, Name: str, Value: str): ...
    class PredefinedMetricSpecification:
        def __init__(self, *, PredefinedMetricType: str, ResourceLabel: str = ...): ...
    class StepAdjustment:
        def __init__(
            self,
            *,
            ScalingAdjustment: int,
            MetricIntervalLowerBound: float = ...,
            MetricIntervalUpperBound: float = ...
        ): ...
    class TargetTrackingConfiguration:
        def __init__(
            self,
            *,
            TargetValue: float,
            CustomizedMetricSpecification: "ScalingPolicy.CustomizedMetricSpecification" = ...,
            DisableScaleIn: bool = ...,
            PredefinedMetricSpecification: "ScalingPolicy.PredefinedMetricSpecification" = ...
        ): ...

class ScheduledAction:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-as-scheduledaction.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AutoScalingGroupName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DesiredCapacity: int = ...,
        EndTime: str = ...,
        MaxSize: int = ...,
        MinSize: int = ...,
        Recurrence: str = ...,
        StartTime: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
