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

_NAMESPACE = "AWS::AppStream"

class DirectoryConfig:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-directoryconfig.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DirectoryName: str,
        OrganizationalUnitDistinguishedNames: List[str],
        ServiceAccountCredentials: "DirectoryConfig.ServiceAccountCredentials",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ServiceAccountCredentials:
        def __init__(self, *, AccountName: str, AccountPassword: str): ...

class Fleet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-fleet.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ComputeCapacity: "Fleet.ComputeCapacity",
        InstanceType: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        DisconnectTimeoutInSeconds: int = ...,
        DisplayName: str = ...,
        DomainJoinInfo: "Fleet.DomainJoinInfo" = ...,
        EnableDefaultInternetAccess: bool = ...,
        FleetType: str = ...,
        IdleDisconnectTimeoutInSeconds: int = ...,
        ImageArn: str = ...,
        ImageName: str = ...,
        MaxUserDurationInSeconds: int = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VpcConfig: "Fleet.VpcConfig" = ...
    ): ...
    class ComputeCapacity:
        def __init__(self, *, DesiredInstances: int): ...
    class DomainJoinInfo:
        def __init__(
            self,
            *,
            DirectoryName: str = ...,
            OrganizationalUnitDistinguishedName: str = ...
        ): ...
    class VpcConfig:
        def __init__(
            self, *, SecurityGroupIds: List[str] = ..., SubnetIds: List[str] = ...
        ): ...

class ImageBuilder:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-imagebuilder.html"""

    StreamingUrl: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        InstanceType: str,
        Name: str,
        AccessEndpoints: List["ImageBuilder.AccessEndpoint"] = ...,
        AppstreamAgentVersion: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        DisplayName: str = ...,
        DomainJoinInfo: "ImageBuilder.DomainJoinInfo" = ...,
        EnableDefaultInternetAccess: bool = ...,
        ImageArn: str = ...,
        ImageName: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VpcConfig: "ImageBuilder.VpcConfig" = ...
    ): ...
    class AccessEndpoint:
        def __init__(self, *, EndpointType: str, VpceId: str): ...
    class DomainJoinInfo:
        def __init__(
            self,
            *,
            DirectoryName: str = ...,
            OrganizationalUnitDistinguishedName: str = ...
        ): ...
    class VpcConfig:
        def __init__(
            self, *, SecurityGroupIds: List[str] = ..., SubnetIds: List[str] = ...
        ): ...

class Stack:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stack.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AccessEndpoints: List["Stack.AccessEndpoint"] = ...,
        ApplicationSettings: "Stack.ApplicationSettings" = ...,
        AttributesToDelete: List[str] = ...,
        DeleteStorageConnectors: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        DisplayName: str = ...,
        EmbedHostDomains: List[str] = ...,
        FeedbackURL: str = ...,
        Name: str = ...,
        RedirectURL: str = ...,
        StorageConnectors: List["Stack.StorageConnector"] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        UserSettings: List["Stack.UserSetting"] = ...
    ): ...
    class AccessEndpoint:
        def __init__(self, *, EndpointType: str, VpceId: str): ...
    class ApplicationSettings:
        def __init__(self, *, Enabled: bool, SettingsGroup: str = ...): ...
    class StorageConnector:
        def __init__(
            self,
            *,
            ConnectorType: str,
            Domains: List[str] = ...,
            ResourceIdentifier: str = ...
        ): ...
    class UserSetting:
        def __init__(self, *, Action: str, Permission: str): ...

class StackFleetAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackfleetassociation.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        FleetName: str,
        StackName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class StackUserAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-stackuserassociation.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AuthenticationType: str,
        StackName: str,
        UserName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        SendEmailNotification: bool = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class User:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appstream-user.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AuthenticationType: str,
        UserName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        FirstName: str = ...,
        LastName: str = ...,
        MessageAction: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
