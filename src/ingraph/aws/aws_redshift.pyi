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

_NAMESPACE = "AWS::Redshift"

class Cluster:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-cluster.html"""

    Endpoint_Address: Final[str]

    Endpoint_Port: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ClusterType: str,
        DBName: str,
        MasterUserPassword: str,
        MasterUsername: str,
        NodeType: str,
        AllowVersionUpgrade: bool = ...,
        AutomatedSnapshotRetentionPeriod: int = ...,
        AvailabilityZone: str = ...,
        ClusterIdentifier: str = ...,
        ClusterParameterGroupName: str = ...,
        ClusterSecurityGroups: List[str] = ...,
        ClusterSubnetGroupName: str = ...,
        ClusterVersion: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ElasticIp: str = ...,
        Encrypted: bool = ...,
        HsmClientCertificateIdentifier: str = ...,
        HsmConfigurationIdentifier: str = ...,
        IamRoles: List[str] = ...,
        KmsKeyId: str = ...,
        LoggingProperties: "Cluster.LoggingProperties" = ...,
        NumberOfNodes: int = ...,
        OwnerAccount: str = ...,
        Port: int = ...,
        PreferredMaintenanceWindow: str = ...,
        PubliclyAccessible: bool = ...,
        SnapshotClusterIdentifier: str = ...,
        SnapshotIdentifier: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VpcSecurityGroupIds: List[str] = ...
    ): ...
    class LoggingProperties:
        def __init__(self, *, BucketName: str, S3KeyPrefix: str = ...): ...

class ClusterParameterGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clusterparametergroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Description: str,
        ParameterGroupFamily: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Parameters: List["ClusterParameterGroup.Parameter"] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Parameter:
        def __init__(self, *, ParameterName: str, ParameterValue: str): ...

class ClusterSecurityGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Description: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ClusterSecurityGroupIngress:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersecuritygroupingress.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ClusterSecurityGroupName: str,
        CIDRIP: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EC2SecurityGroupName: str = ...,
        EC2SecurityGroupOwnerId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ClusterSubnetGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-redshift-clustersubnetgroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Description: str,
        SubnetIds: List[str],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
