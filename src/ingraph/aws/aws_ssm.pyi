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

_NAMESPACE = "AWS::SSM"

class Association:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-association.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        AssociationName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DocumentVersion: str = ...,
        InstanceId: str = ...,
        OutputLocation: "Association.InstanceAssociationOutputLocation" = ...,
        Parameters: Dict[str, "Association.ParameterValues"] = ...,
        ScheduleExpression: str = ...,
        Targets: List["Association.Target"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class InstanceAssociationOutputLocation:
        def __init__(self, *, S3Location: "Association.S3OutputLocation" = ...): ...
    class ParameterValues:
        def __init__(self, *, ParameterValues: List[str]): ...
    class S3OutputLocation:
        def __init__(
            self, *, OutputS3BucketName: str = ..., OutputS3KeyPrefix: str = ...
        ): ...
    class Target:
        def __init__(self, *, Key: str, Values: List[str]): ...

class Document:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-document.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Content: Any,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DocumentType: str = ...,
        Name: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class MaintenanceWindow:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindow.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AllowUnassociatedTargets: bool,
        Cutoff: int,
        Duration: int,
        Name: str,
        Schedule: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        EndDate: str = ...,
        ScheduleTimezone: str = ...,
        StartDate: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class MaintenanceWindowTarget:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtarget.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ResourceType: str,
        Targets: List["MaintenanceWindowTarget.Targets"],
        WindowId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Name: str = ...,
        OwnerInformation: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Targets:
        def __init__(self, *, Key: str, Values: List[str] = ...): ...

class MaintenanceWindowTask:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-maintenancewindowtask.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        MaxConcurrency: str,
        MaxErrors: str,
        Priority: int,
        Targets: List["MaintenanceWindowTask.Target"],
        TaskArn: str,
        TaskType: str,
        WindowId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        LoggingInfo: "MaintenanceWindowTask.LoggingInfo" = ...,
        Name: str = ...,
        ServiceRoleArn: str = ...,
        TaskInvocationParameters: "MaintenanceWindowTask.TaskInvocationParameters" = ...,
        TaskParameters: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class LoggingInfo:
        def __init__(self, *, Region: str, S3Bucket: str, S3Prefix: str = ...): ...
    class MaintenanceWindowAutomationParameters:
        def __init__(self, *, DocumentVersion: str = ..., Parameters: Any = ...): ...
    class MaintenanceWindowLambdaParameters:
        def __init__(
            self, *, ClientContext: str = ..., Payload: str = ..., Qualifier: str = ...
        ): ...
    class MaintenanceWindowRunCommandParameters:
        def __init__(
            self,
            *,
            Comment: str = ...,
            DocumentHash: str = ...,
            DocumentHashType: str = ...,
            NotificationConfig: "MaintenanceWindowTask.NotificationConfig" = ...,
            OutputS3BucketName: str = ...,
            OutputS3KeyPrefix: str = ...,
            Parameters: Any = ...,
            ServiceRoleArn: str = ...,
            TimeoutSeconds: int = ...
        ): ...
    class MaintenanceWindowStepFunctionsParameters:
        def __init__(self, *, Input: str = ..., Name: str = ...): ...
    class NotificationConfig:
        def __init__(
            self,
            *,
            NotificationArn: str,
            NotificationEvents: List[str] = ...,
            NotificationType: str = ...
        ): ...
    class Target:
        def __init__(self, *, Key: str, Values: List[str] = ...): ...
    class TaskInvocationParameters:
        def __init__(
            self,
            *,
            MaintenanceWindowAutomationParameters: "MaintenanceWindowTask.MaintenanceWindowAutomationParameters" = ...,
            MaintenanceWindowLambdaParameters: "MaintenanceWindowTask.MaintenanceWindowLambdaParameters" = ...,
            MaintenanceWindowRunCommandParameters: "MaintenanceWindowTask.MaintenanceWindowRunCommandParameters" = ...,
            MaintenanceWindowStepFunctionsParameters: "MaintenanceWindowTask.MaintenanceWindowStepFunctionsParameters" = ...
        ): ...

class Parameter:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html"""

    Type: Final[str]

    Value: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Type: str,
        Value: str,
        AllowedPattern: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Name: str = ...,
        Policies: str = ...,
        Tags: Any = ...,
        Tier: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class PatchBaseline:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-patchbaseline.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        ApprovalRules: "PatchBaseline.RuleGroup" = ...,
        ApprovedPatches: List[str] = ...,
        ApprovedPatchesComplianceLevel: str = ...,
        ApprovedPatchesEnableNonSecurity: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        GlobalFilters: "PatchBaseline.PatchFilterGroup" = ...,
        OperatingSystem: str = ...,
        PatchGroups: List[str] = ...,
        RejectedPatches: List[str] = ...,
        RejectedPatchesAction: str = ...,
        Sources: List["PatchBaseline.PatchSource"] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class PatchFilter:
        def __init__(self, *, Key: str = ..., Values: List[str] = ...): ...
    class PatchFilterGroup:
        def __init__(
            self, *, PatchFilters: List["PatchBaseline.PatchFilter"] = ...
        ): ...
    class PatchSource:
        def __init__(
            self,
            *,
            Configuration: str = ...,
            Name: str = ...,
            Products: List[str] = ...
        ): ...
    class Rule:
        def __init__(
            self,
            *,
            ApproveAfterDays: int = ...,
            ComplianceLevel: str = ...,
            EnableNonSecurity: bool = ...,
            PatchFilterGroup: "PatchBaseline.PatchFilterGroup" = ...
        ): ...
    class RuleGroup:
        def __init__(self, *, PatchRules: List["PatchBaseline.Rule"] = ...): ...

class ResourceDataSync:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        SyncName: str,
        BucketName: str = ...,
        BucketPrefix: str = ...,
        BucketRegion: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        KMSKeyArn: str = ...,
        S3Destination: "ResourceDataSync.S3Destination" = ...,
        SyncFormat: str = ...,
        SyncSource: "ResourceDataSync.SyncSource" = ...,
        SyncType: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AwsOrganizationsSource:
        def __init__(
            self, *, OrganizationSourceType: str, OrganizationalUnits: List[str] = ...
        ): ...
    class S3Destination:
        def __init__(
            self,
            *,
            BucketName: str,
            BucketRegion: str,
            SyncFormat: str,
            BucketPrefix: str = ...,
            KMSKeyArn: str = ...
        ): ...
    class SyncSource:
        def __init__(
            self,
            *,
            SourceRegions: List[str],
            SourceType: str,
            AwsOrganizationsSource: "ResourceDataSync.AwsOrganizationsSource" = ...,
            IncludeFutureRegions: bool = ...
        ): ...
