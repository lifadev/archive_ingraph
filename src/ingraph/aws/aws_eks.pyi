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

_NAMESPACE = "AWS::EKS"

class Cluster:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-cluster.html"""

    Endpoint: Final[str]

    ClusterSecurityGroupId: Final[str]

    EncryptionConfigKeyArn: Final[str]

    Arn: Final[str]

    CertificateAuthorityData: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ResourcesVpcConfig: "Cluster.ResourcesVpcConfig",
        RoleArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EncryptionConfig: List["Cluster.EncryptionConfig"] = ...,
        Name: str = ...,
        UpdateReplacePolicy: str = ...,
        Version: str = ...
    ): ...
    class EncryptionConfig:
        def __init__(
            self, *, Provider: "Cluster.Provider" = ..., Resources: List[str] = ...
        ): ...
    class Provider:
        def __init__(self, *, KeyArn: str = ...): ...
    class ResourcesVpcConfig:
        def __init__(
            self, *, SubnetIds: List[str], SecurityGroupIds: List[str] = ...
        ): ...

class Nodegroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eks-nodegroup.html"""

    NodegroupName: Final[str]

    ClusterName: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ClusterName: str,
        NodeRole: str,
        Subnets: List[str],
        AmiType: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DiskSize: float = ...,
        ForceUpdateEnabled: bool = ...,
        InstanceTypes: List[str] = ...,
        Labels: Any = ...,
        NodegroupName: str = ...,
        ReleaseVersion: str = ...,
        RemoteAccess: "Nodegroup.RemoteAccess" = ...,
        ScalingConfig: "Nodegroup.ScalingConfig" = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...,
        Version: str = ...
    ): ...
    class RemoteAccess:
        def __init__(
            self, *, Ec2SshKey: str, SourceSecurityGroups: List[str] = ...
        ): ...
    class ScalingConfig:
        def __init__(
            self,
            *,
            DesiredSize: float = ...,
            MaxSize: float = ...,
            MinSize: float = ...
        ): ...
