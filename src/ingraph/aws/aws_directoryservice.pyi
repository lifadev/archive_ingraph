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

_NAMESPACE = "AWS::DirectoryService"

class MicrosoftAD:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html"""

    Alias: Final[str]

    DnsIpAddresses: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        Password: str,
        VpcSettings: "MicrosoftAD.VpcSettings",
        CreateAlias: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Edition: str = ...,
        EnableSso: bool = ...,
        ShortName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class VpcSettings:
        def __init__(self, *, SubnetIds: List[str], VpcId: str): ...

class SimpleAD:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html"""

    Alias: Final[str]

    DnsIpAddresses: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        Password: str,
        Size: str,
        VpcSettings: "SimpleAD.VpcSettings",
        CreateAlias: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        EnableSso: bool = ...,
        ShortName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class VpcSettings:
        def __init__(self, *, SubnetIds: List[str], VpcId: str): ...
