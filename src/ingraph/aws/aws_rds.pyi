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

_NAMESPACE = "AWS::RDS"

class DBCluster:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html"""

    Endpoint_Address: Final[str]

    Endpoint_Port: Final[str]

    ReadEndpoint_Address: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Engine: str,
        AssociatedRoles: List["DBCluster.DBClusterRole"] = ...,
        AvailabilityZones: List[str] = ...,
        BacktrackWindow: int = ...,
        BackupRetentionPeriod: int = ...,
        DBClusterIdentifier: str = ...,
        DBClusterParameterGroupName: str = ...,
        DBSubnetGroupName: str = ...,
        DatabaseName: str = ...,
        DeletionPolicy: str = ...,
        DeletionProtection: bool = ...,
        DependsOn: List[Any] = ...,
        EnableCloudwatchLogsExports: List[str] = ...,
        EnableHttpEndpoint: bool = ...,
        EnableIAMDatabaseAuthentication: bool = ...,
        EngineMode: str = ...,
        EngineVersion: str = ...,
        KmsKeyId: str = ...,
        MasterUserPassword: str = ...,
        MasterUsername: str = ...,
        Port: int = ...,
        PreferredBackupWindow: str = ...,
        PreferredMaintenanceWindow: str = ...,
        ReplicationSourceIdentifier: str = ...,
        RestoreType: str = ...,
        ScalingConfiguration: "DBCluster.ScalingConfiguration" = ...,
        SnapshotIdentifier: str = ...,
        SourceDBClusterIdentifier: str = ...,
        SourceRegion: str = ...,
        StorageEncrypted: bool = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        UseLatestRestorableTime: bool = ...,
        VpcSecurityGroupIds: List[str] = ...
    ): ...
    class DBClusterRole:
        def __init__(self, *, RoleArn: str, FeatureName: str = ...): ...
    class ScalingConfiguration:
        def __init__(
            self,
            *,
            AutoPause: bool = ...,
            MaxCapacity: int = ...,
            MinCapacity: int = ...,
            SecondsUntilAutoPause: int = ...
        ): ...

class DBClusterParameterGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbclusterparametergroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Description: str,
        Family: str,
        Parameters: Any,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class DBInstance:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html"""

    Endpoint_Address: Final[str]

    Endpoint_Port: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DBInstanceClass: str,
        AllocatedStorage: str = ...,
        AllowMajorVersionUpgrade: bool = ...,
        AssociatedRoles: List["DBInstance.DBInstanceRole"] = ...,
        AutoMinorVersionUpgrade: bool = ...,
        AvailabilityZone: str = ...,
        BackupRetentionPeriod: int = ...,
        CACertificateIdentifier: str = ...,
        CharacterSetName: str = ...,
        CopyTagsToSnapshot: bool = ...,
        DBClusterIdentifier: str = ...,
        DBInstanceIdentifier: str = ...,
        DBName: str = ...,
        DBParameterGroupName: str = ...,
        DBSecurityGroups: List[str] = ...,
        DBSnapshotIdentifier: str = ...,
        DBSubnetGroupName: str = ...,
        DeleteAutomatedBackups: bool = ...,
        DeletionPolicy: str = ...,
        DeletionProtection: bool = ...,
        DependsOn: List[Any] = ...,
        Domain: str = ...,
        DomainIAMRoleName: str = ...,
        EnableCloudwatchLogsExports: List[str] = ...,
        EnableIAMDatabaseAuthentication: bool = ...,
        EnablePerformanceInsights: bool = ...,
        Engine: str = ...,
        EngineVersion: str = ...,
        Iops: int = ...,
        KmsKeyId: str = ...,
        LicenseModel: str = ...,
        MasterUserPassword: str = ...,
        MasterUsername: str = ...,
        MaxAllocatedStorage: int = ...,
        MonitoringInterval: int = ...,
        MonitoringRoleArn: str = ...,
        MultiAZ: bool = ...,
        OptionGroupName: str = ...,
        PerformanceInsightsKMSKeyId: str = ...,
        PerformanceInsightsRetentionPeriod: int = ...,
        Port: str = ...,
        PreferredBackupWindow: str = ...,
        PreferredMaintenanceWindow: str = ...,
        ProcessorFeatures: List["DBInstance.ProcessorFeature"] = ...,
        PromotionTier: int = ...,
        PubliclyAccessible: bool = ...,
        SourceDBInstanceIdentifier: str = ...,
        SourceRegion: str = ...,
        StorageEncrypted: bool = ...,
        StorageType: str = ...,
        Tags: List["Tag"] = ...,
        Timezone: str = ...,
        UpdateReplacePolicy: str = ...,
        UseDefaultProcessorFeatures: bool = ...,
        VPCSecurityGroups: List[str] = ...
    ): ...
    class DBInstanceRole:
        def __init__(self, *, FeatureName: str, RoleArn: str): ...
    class ProcessorFeature:
        def __init__(self, *, Name: str = ..., Value: str = ...): ...

class DBParameterGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Description: str,
        Family: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Parameters: Dict[str, str] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class DBSecurityGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-security-group.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DBSecurityGroupIngress: List["DBSecurityGroup.Ingress"],
        GroupDescription: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EC2VpcId: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Ingress:
        def __init__(
            self,
            *,
            CIDRIP: str = ...,
            EC2SecurityGroupId: str = ...,
            EC2SecurityGroupName: str = ...,
            EC2SecurityGroupOwnerId: str = ...
        ): ...

class DBSecurityGroupIngress:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-security-group-ingress.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DBSecurityGroupName: str,
        CIDRIP: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EC2SecurityGroupId: str = ...,
        EC2SecurityGroupName: str = ...,
        EC2SecurityGroupOwnerId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class DBSubnetGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbsubnet-group.html"""

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

class EventSubscription:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-eventsubscription.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        SnsTopicArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Enabled: bool = ...,
        EventCategories: List[str] = ...,
        SourceIds: List[str] = ...,
        SourceType: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class OptionGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        EngineName: str,
        MajorEngineVersion: str,
        OptionConfigurations: List["OptionGroup.OptionConfiguration"],
        OptionGroupDescription: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class OptionConfiguration:
        def __init__(
            self,
            *,
            OptionName: str,
            DBSecurityGroupMemberships: List[str] = ...,
            OptionSettings: List["OptionGroup.OptionSetting"] = ...,
            OptionVersion: str = ...,
            Port: int = ...,
            VpcSecurityGroupMemberships: List[str] = ...
        ): ...
    class OptionSetting:
        def __init__(self, *, Name: str = ..., Value: str = ...): ...
