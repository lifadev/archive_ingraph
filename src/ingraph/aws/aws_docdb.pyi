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

_NAMESPACE = "AWS::DocDB"

class DBCluster:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbcluster.html"""

    ClusterResourceId: Final[str]

    Endpoint: Final[str]

    Port: Final[str]

    ReadEndpoint: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        MasterUserPassword: str,
        MasterUsername: str,
        AvailabilityZones: List[str] = ...,
        BackupRetentionPeriod: int = ...,
        DBClusterIdentifier: str = ...,
        DBClusterParameterGroupName: str = ...,
        DBSubnetGroupName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EnableCloudwatchLogsExports: List[str] = ...,
        EngineVersion: str = ...,
        KmsKeyId: str = ...,
        Port: int = ...,
        PreferredBackupWindow: str = ...,
        PreferredMaintenanceWindow: str = ...,
        SnapshotIdentifier: str = ...,
        StorageEncrypted: bool = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VpcSecurityGroupIds: List[str] = ...
    ): ...

class DBClusterParameterGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbclusterparametergroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Description: str,
        Family: str,
        Parameters: Any,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class DBInstance:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbinstance.html"""

    Endpoint: Final[str]

    Port: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DBClusterIdentifier: str,
        DBInstanceClass: str,
        AutoMinorVersionUpgrade: bool = ...,
        AvailabilityZone: str = ...,
        DBInstanceIdentifier: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        PreferredMaintenanceWindow: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class DBSubnetGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-docdb-dbsubnetgroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DBSubnetGroupDescription: str,
        SubnetIds: List[str],
        DBSubnetGroupName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
