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

_NAMESPACE = "AWS::FSx"

class FileSystem:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fsx-filesystem.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        FileSystemType: str,
        SubnetIds: List[str],
        BackupId: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        KmsKeyId: str = ...,
        LustreConfiguration: "FileSystem.LustreConfiguration" = ...,
        SecurityGroupIds: List[str] = ...,
        StorageCapacity: int = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        WindowsConfiguration: "FileSystem.WindowsConfiguration" = ...
    ): ...
    class LustreConfiguration:
        def __init__(
            self,
            *,
            DeploymentType: str = ...,
            ExportPath: str = ...,
            ImportPath: str = ...,
            ImportedFileChunkSize: int = ...,
            PerUnitStorageThroughput: int = ...,
            WeeklyMaintenanceStartTime: str = ...
        ): ...
    class SelfManagedActiveDirectoryConfiguration:
        def __init__(
            self,
            *,
            DnsIps: List[str] = ...,
            DomainName: str = ...,
            FileSystemAdministratorsGroup: str = ...,
            OrganizationalUnitDistinguishedName: str = ...,
            Password: str = ...,
            UserName: str = ...
        ): ...
    class WindowsConfiguration:
        def __init__(
            self,
            *,
            ActiveDirectoryId: str = ...,
            AutomaticBackupRetentionDays: int = ...,
            CopyTagsToBackups: bool = ...,
            DailyAutomaticBackupStartTime: str = ...,
            DeploymentType: str = ...,
            PreferredSubnetId: str = ...,
            SelfManagedActiveDirectoryConfiguration: "FileSystem.SelfManagedActiveDirectoryConfiguration" = ...,
            ThroughputCapacity: int = ...,
            WeeklyMaintenanceStartTime: str = ...
        ): ...
