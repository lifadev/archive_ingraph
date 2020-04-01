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

_NAMESPACE = "AWS::CodeDeploy"

class Application:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationName: str = ...,
        ComputePlatform: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class DeploymentConfig:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DeploymentConfigName: str = ...,
        MinimumHealthyHosts: "DeploymentConfig.MinimumHealthyHosts" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class MinimumHealthyHosts:
        def __init__(self, *, Type: str, Value: int): ...

class DeploymentGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApplicationName: str,
        ServiceRoleArn: str,
        AlarmConfiguration: "DeploymentGroup.AlarmConfiguration" = ...,
        AutoRollbackConfiguration: "DeploymentGroup.AutoRollbackConfiguration" = ...,
        AutoScalingGroups: List[str] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Deployment: "DeploymentGroup.Deployment" = ...,
        DeploymentConfigName: str = ...,
        DeploymentGroupName: str = ...,
        DeploymentStyle: "DeploymentGroup.DeploymentStyle" = ...,
        Ec2TagFilters: List["DeploymentGroup.EC2TagFilter"] = ...,
        Ec2TagSet: "DeploymentGroup.EC2TagSet" = ...,
        LoadBalancerInfo: "DeploymentGroup.LoadBalancerInfo" = ...,
        OnPremisesInstanceTagFilters: List["DeploymentGroup.TagFilter"] = ...,
        OnPremisesTagSet: "DeploymentGroup.OnPremisesTagSet" = ...,
        TriggerConfigurations: List["DeploymentGroup.TriggerConfig"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Alarm:
        def __init__(self, *, Name: str = ...): ...
    class AlarmConfiguration:
        def __init__(
            self,
            *,
            Alarms: List["DeploymentGroup.Alarm"] = ...,
            Enabled: bool = ...,
            IgnorePollAlarmFailure: bool = ...
        ): ...
    class AutoRollbackConfiguration:
        def __init__(self, *, Enabled: bool = ..., Events: List[str] = ...): ...
    class Deployment:
        def __init__(
            self,
            *,
            Revision: "DeploymentGroup.RevisionLocation",
            Description: str = ...,
            IgnoreApplicationStopFailures: bool = ...
        ): ...
    class DeploymentStyle:
        def __init__(
            self, *, DeploymentOption: str = ..., DeploymentType: str = ...
        ): ...
    class EC2TagFilter:
        def __init__(self, *, Key: str = ..., Type: str = ..., Value: str = ...): ...
    class EC2TagSet:
        def __init__(
            self, *, Ec2TagSetList: List["DeploymentGroup.EC2TagSetListObject"] = ...
        ): ...
    class EC2TagSetListObject:
        def __init__(
            self, *, Ec2TagGroup: List["DeploymentGroup.EC2TagFilter"] = ...
        ): ...
    class ELBInfo:
        def __init__(self, *, Name: str = ...): ...
    class GitHubLocation:
        def __init__(self, *, CommitId: str, Repository: str): ...
    class LoadBalancerInfo:
        def __init__(
            self,
            *,
            ElbInfoList: List["DeploymentGroup.ELBInfo"] = ...,
            TargetGroupInfoList: List["DeploymentGroup.TargetGroupInfo"] = ...
        ): ...
    class OnPremisesTagSet:
        def __init__(
            self,
            *,
            OnPremisesTagSetList: List[
                "DeploymentGroup.OnPremisesTagSetListObject"
            ] = ...
        ): ...
    class OnPremisesTagSetListObject:
        def __init__(
            self, *, OnPremisesTagGroup: List["DeploymentGroup.TagFilter"] = ...
        ): ...
    class RevisionLocation:
        def __init__(
            self,
            *,
            GitHubLocation: "DeploymentGroup.GitHubLocation" = ...,
            RevisionType: str = ...,
            S3Location: "DeploymentGroup.S3Location" = ...
        ): ...
    class S3Location:
        def __init__(
            self,
            *,
            Bucket: str,
            Key: str,
            BundleType: str = ...,
            ETag: str = ...,
            Version: str = ...
        ): ...
    class TagFilter:
        def __init__(self, *, Key: str = ..., Type: str = ..., Value: str = ...): ...
    class TargetGroupInfo:
        def __init__(self, *, Name: str = ...): ...
    class TriggerConfig:
        def __init__(
            self,
            *,
            TriggerEvents: List[str] = ...,
            TriggerName: str = ...,
            TriggerTargetArn: str = ...
        ): ...
