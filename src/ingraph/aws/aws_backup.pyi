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

_NAMESPACE = "AWS::Backup"

class BackupPlan:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html"""

    VersionId: Final[str]

    BackupPlanId: Final[str]

    BackupPlanArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        BackupPlan: "BackupPlan.BackupPlanResourceType",
        BackupPlanTags: Any = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class BackupPlanResourceType:
        def __init__(
            self,
            *,
            BackupPlanName: str,
            BackupPlanRule: List["BackupPlan.BackupRuleResourceType"]
        ): ...
    class BackupRuleResourceType:
        def __init__(
            self,
            *,
            RuleName: str,
            TargetBackupVault: str,
            CompletionWindowMinutes: float = ...,
            CopyActions: List["BackupPlan.CopyActionResourceType"] = ...,
            Lifecycle: "BackupPlan.LifecycleResourceType" = ...,
            RecoveryPointTags: Any = ...,
            ScheduleExpression: str = ...,
            StartWindowMinutes: float = ...
        ): ...
    class CopyActionResourceType:
        def __init__(
            self,
            *,
            DestinationBackupVaultArn: str,
            Lifecycle: "BackupPlan.LifecycleResourceType" = ...
        ): ...
    class LifecycleResourceType:
        def __init__(
            self,
            *,
            DeleteAfterDays: float = ...,
            MoveToColdStorageAfterDays: float = ...
        ): ...

class BackupSelection:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupselection.html"""

    BackupPlanId: Final[str]

    SelectionId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        BackupPlanId: str,
        BackupSelection: "BackupSelection.BackupSelectionResourceType",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class BackupSelectionResourceType:
        def __init__(
            self,
            *,
            IamRoleArn: str,
            SelectionName: str,
            ListOfTags: List["BackupSelection.ConditionResourceType"] = ...,
            Resources: List[str] = ...
        ): ...
    class ConditionResourceType:
        def __init__(
            self, *, ConditionKey: str, ConditionType: str, ConditionValue: str
        ): ...

class BackupVault:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupvault.html"""

    BackupVaultName: Final[str]

    BackupVaultArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        BackupVaultName: str,
        AccessPolicy: Any = ...,
        BackupVaultTags: Any = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EncryptionKeyArn: str = ...,
        Notifications: "BackupVault.NotificationObjectType" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class NotificationObjectType:
        def __init__(self, *, BackupVaultEvents: List[str], SNSTopicArn: str): ...
