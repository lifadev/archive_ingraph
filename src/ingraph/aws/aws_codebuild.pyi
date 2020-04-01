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

_NAMESPACE = "AWS::CodeBuild"

class Project:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-project.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Artifacts: "Project.Artifacts",
        Environment: "Project.Environment",
        ServiceRole: str,
        Source: "Project.Source",
        BadgeEnabled: bool = ...,
        Cache: "Project.ProjectCache" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        EncryptionKey: str = ...,
        FileSystemLocations: List["Project.ProjectFileSystemLocation"] = ...,
        LogsConfig: "Project.LogsConfig" = ...,
        Name: str = ...,
        QueuedTimeoutInMinutes: int = ...,
        SecondaryArtifacts: List["Project.Artifacts"] = ...,
        SecondarySourceVersions: List["Project.ProjectSourceVersion"] = ...,
        SecondarySources: List["Project.Source"] = ...,
        SourceVersion: str = ...,
        Tags: List["Tag"] = ...,
        TimeoutInMinutes: int = ...,
        Triggers: "Project.ProjectTriggers" = ...,
        UpdateReplacePolicy: str = ...,
        VpcConfig: "Project.VpcConfig" = ...
    ): ...
    class Artifacts:
        def __init__(
            self,
            *,
            Type: str,
            ArtifactIdentifier: str = ...,
            EncryptionDisabled: bool = ...,
            Location: str = ...,
            Name: str = ...,
            NamespaceType: str = ...,
            OverrideArtifactName: bool = ...,
            Packaging: str = ...,
            Path: str = ...
        ): ...
    class CloudWatchLogsConfig:
        def __init__(
            self, *, Status: str, GroupName: str = ..., StreamName: str = ...
        ): ...
    class Environment:
        def __init__(
            self,
            *,
            ComputeType: str,
            Image: str,
            Type: str,
            Certificate: str = ...,
            EnvironmentVariables: List["Project.EnvironmentVariable"] = ...,
            ImagePullCredentialsType: str = ...,
            PrivilegedMode: bool = ...,
            RegistryCredential: "Project.RegistryCredential" = ...
        ): ...
    class EnvironmentVariable:
        def __init__(self, *, Name: str, Value: str, Type: str = ...): ...
    class FilterGroup:
        def __init__(self) -> None: ...
    class GitSubmodulesConfig:
        def __init__(self, *, FetchSubmodules: bool): ...
    class LogsConfig:
        def __init__(
            self,
            *,
            CloudWatchLogs: "Project.CloudWatchLogsConfig" = ...,
            S3Logs: "Project.S3LogsConfig" = ...
        ): ...
    class ProjectCache:
        def __init__(
            self, *, Type: str, Location: str = ..., Modes: List[str] = ...
        ): ...
    class ProjectFileSystemLocation:
        def __init__(
            self,
            *,
            Identifier: str,
            Location: str,
            MountPoint: str,
            Type: str,
            MountOptions: str = ...
        ): ...
    class ProjectSourceVersion:
        def __init__(self, *, SourceIdentifier: str, SourceVersion: str = ...): ...
    class ProjectTriggers:
        def __init__(
            self,
            *,
            FilterGroups: List["Project.FilterGroup"] = ...,
            Webhook: bool = ...
        ): ...
    class RegistryCredential:
        def __init__(self, *, Credential: str, CredentialProvider: str): ...
    class S3LogsConfig:
        def __init__(
            self, *, Status: str, EncryptionDisabled: bool = ..., Location: str = ...
        ): ...
    class Source:
        def __init__(
            self,
            *,
            Type: str,
            Auth: "Project.SourceAuth" = ...,
            BuildSpec: str = ...,
            GitCloneDepth: int = ...,
            GitSubmodulesConfig: "Project.GitSubmodulesConfig" = ...,
            InsecureSsl: bool = ...,
            Location: str = ...,
            ReportBuildStatus: bool = ...,
            SourceIdentifier: str = ...
        ): ...
    class SourceAuth:
        def __init__(self, *, Type: str, Resource: str = ...): ...
    class VpcConfig:
        def __init__(
            self,
            *,
            SecurityGroupIds: List[str] = ...,
            Subnets: List[str] = ...,
            VpcId: str = ...
        ): ...
    class WebhookFilter:
        def __init__(
            self, *, Pattern: str, Type: str, ExcludeMatchedPattern: bool = ...
        ): ...

class ReportGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-reportgroup.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ExportConfig: "ReportGroup.ReportExportConfig",
        Type: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ReportExportConfig:
        def __init__(
            self,
            *,
            ExportConfigType: str,
            S3Destination: "ReportGroup.S3ReportExportConfig" = ...
        ): ...
    class S3ReportExportConfig:
        def __init__(
            self,
            *,
            Bucket: str,
            EncryptionDisabled: bool = ...,
            EncryptionKey: str = ...,
            Packaging: str = ...,
            Path: str = ...
        ): ...

class SourceCredential:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codebuild-sourcecredential.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AuthType: str,
        ServerType: str,
        Token: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...,
        Username: str = ...
    ): ...
