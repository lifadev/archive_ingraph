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

_NAMESPACE = "AWS::IAM"

class AccessKey:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"""

    SecretAccessKey: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        UserName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Serial: int = ...,
        Status: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Group:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        GroupName: str = ...,
        ManagedPolicyArns: List[str] = ...,
        Path: str = ...,
        Policies: List["Group.Policy"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Policy:
        def __init__(self, *, PolicyDocument: Any, PolicyName: str): ...

class InstanceProfile:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Roles: List[str],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InstanceProfileName: str = ...,
        Path: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ManagedPolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-managedpolicy.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PolicyDocument: Any,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Groups: List[str] = ...,
        ManagedPolicyName: str = ...,
        Path: str = ...,
        Roles: List[str] = ...,
        UpdateReplacePolicy: str = ...,
        Users: List[str] = ...
    ): ...

class Policy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PolicyDocument: Any,
        PolicyName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Groups: List[str] = ...,
        Roles: List[str] = ...,
        UpdateReplacePolicy: str = ...,
        Users: List[str] = ...
    ): ...

class Role:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"""

    Arn: Final[str]

    RoleId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AssumeRolePolicyDocument: Any,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        ManagedPolicyArns: List[str] = ...,
        MaxSessionDuration: int = ...,
        Path: str = ...,
        PermissionsBoundary: str = ...,
        Policies: List["Role.Policy"] = ...,
        RoleName: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Policy:
        def __init__(self, *, PolicyDocument: Any, PolicyName: str): ...

class ServiceLinkedRole:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-servicelinkedrole.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AWSServiceName: str,
        CustomSuffix: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class User:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Groups: List[str] = ...,
        LoginProfile: "User.LoginProfile" = ...,
        ManagedPolicyArns: List[str] = ...,
        Path: str = ...,
        PermissionsBoundary: str = ...,
        Policies: List["User.Policy"] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        UserName: str = ...
    ): ...
    class LoginProfile:
        def __init__(self, *, Password: str, PasswordResetRequired: bool = ...): ...
    class Policy:
        def __init__(self, *, PolicyDocument: Any, PolicyName: str): ...

class UserToGroupAddition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        GroupName: str,
        Users: List[str],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
