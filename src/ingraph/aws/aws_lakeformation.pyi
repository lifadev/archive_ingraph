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

_NAMESPACE = "AWS::LakeFormation"

class DataLakeSettings:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-datalakesettings.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Admins: "DataLakeSettings.Admins" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Admins:
        def __init__(self) -> None: ...
    class DataLakePrincipal:
        def __init__(self, *, DataLakePrincipalIdentifier: str = ...): ...

class Permissions:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-permissions.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DataLakePrincipal: "Permissions.DataLakePrincipal",
        Resource: "Permissions.Resource",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Permissions: List[str] = ...,
        PermissionsWithGrantOption: List[str] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ColumnWildcard:
        def __init__(self, *, ExcludedColumnNames: List[str] = ...): ...
    class DataLakePrincipal:
        def __init__(self, *, DataLakePrincipalIdentifier: str = ...): ...
    class DataLocationResource:
        def __init__(self, *, S3Resource: str = ...): ...
    class DatabaseResource:
        def __init__(self, *, Name: str = ...): ...
    class Resource:
        def __init__(
            self,
            *,
            DataLocationResource: "Permissions.DataLocationResource" = ...,
            DatabaseResource: "Permissions.DatabaseResource" = ...,
            TableResource: "Permissions.TableResource" = ...,
            TableWithColumnsResource: "Permissions.TableWithColumnsResource" = ...
        ): ...
    class TableResource:
        def __init__(self, *, DatabaseName: str = ..., Name: str = ...): ...
    class TableWithColumnsResource:
        def __init__(
            self,
            *,
            ColumnNames: List[str] = ...,
            ColumnWildcard: "Permissions.ColumnWildcard" = ...,
            DatabaseName: str = ...,
            Name: str = ...
        ): ...

class Resource:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lakeformation-resource.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ResourceArn: str,
        UseServiceLinkedRole: bool,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RoleArn: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
