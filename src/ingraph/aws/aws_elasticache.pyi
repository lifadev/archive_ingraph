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

_NAMESPACE = "AWS::ElastiCache"

class CacheCluster:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-cache-cluster.html"""

    ConfigurationEndpoint_Address: Final[str]

    ConfigurationEndpoint_Port: Final[str]

    RedisEndpoint_Address: Final[str]

    RedisEndpoint_Port: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        CacheNodeType: str,
        Engine: str,
        NumCacheNodes: int,
        AZMode: str = ...,
        AutoMinorVersionUpgrade: bool = ...,
        CacheParameterGroupName: str = ...,
        CacheSecurityGroupNames: List[str] = ...,
        CacheSubnetGroupName: str = ...,
        ClusterName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EngineVersion: str = ...,
        NotificationTopicArn: str = ...,
        Port: int = ...,
        PreferredAvailabilityZone: str = ...,
        PreferredAvailabilityZones: List[str] = ...,
        PreferredMaintenanceWindow: str = ...,
        SnapshotArns: List[str] = ...,
        SnapshotName: str = ...,
        SnapshotRetentionLimit: int = ...,
        SnapshotWindow: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VpcSecurityGroupIds: List[str] = ...
    ): ...

class ParameterGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-parameter-group.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CacheParameterGroupFamily: str,
        Description: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Properties: Dict[str, str] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ReplicationGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticache-replicationgroup.html"""

    ConfigurationEndPoint_Address: Final[str]

    ConfigurationEndPoint_Port: Final[str]

    PrimaryEndPoint_Address: Final[str]

    PrimaryEndPoint_Port: Final[str]

    ReadEndPoint_Addresses: Final[str]

    ReadEndPoint_Addresses_List: Final[List[str]]

    ReadEndPoint_Ports: Final[str]

    ReadEndPoint_Ports_List: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ReplicationGroupDescription: str,
        AtRestEncryptionEnabled: bool = ...,
        AuthToken: str = ...,
        AutoMinorVersionUpgrade: bool = ...,
        AutomaticFailoverEnabled: bool = ...,
        CacheNodeType: str = ...,
        CacheParameterGroupName: str = ...,
        CacheSecurityGroupNames: List[str] = ...,
        CacheSubnetGroupName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Engine: str = ...,
        EngineVersion: str = ...,
        KmsKeyId: str = ...,
        NodeGroupConfiguration: List["ReplicationGroup.NodeGroupConfiguration"] = ...,
        NotificationTopicArn: str = ...,
        NumCacheClusters: int = ...,
        NumNodeGroups: int = ...,
        Port: int = ...,
        PreferredCacheClusterAZs: List[str] = ...,
        PreferredMaintenanceWindow: str = ...,
        PrimaryClusterId: str = ...,
        ReplicasPerNodeGroup: int = ...,
        ReplicationGroupId: str = ...,
        SecurityGroupIds: List[str] = ...,
        SnapshotArns: List[str] = ...,
        SnapshotName: str = ...,
        SnapshotRetentionLimit: int = ...,
        SnapshotWindow: str = ...,
        SnapshottingClusterId: str = ...,
        Tags: List["Tag"] = ...,
        TransitEncryptionEnabled: bool = ...,
        UpdatePolicy: "ReplicationGroup.UpdatePolicy" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class NodeGroupConfiguration:
        def __init__(
            self,
            *,
            NodeGroupId: str = ...,
            PrimaryAvailabilityZone: str = ...,
            ReplicaAvailabilityZones: List[str] = ...,
            ReplicaCount: int = ...,
            Slots: str = ...
        ): ...
    class UpdatePolicy:
        def __init__(self, *, UseOnlineResharding: bool = ...): ...

class SecurityGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Description: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class SecurityGroupIngress:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-security-group-ingress.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CacheSecurityGroupName: str,
        EC2SecurityGroupName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EC2SecurityGroupOwnerId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class SubnetGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-subnetgroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Description: str,
        SubnetIds: List[str],
        CacheSubnetGroupName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
