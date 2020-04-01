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

_NAMESPACE = "AWS::Transfer"

class Server:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html"""

    ServerId: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EndpointDetails: "Server.EndpointDetails" = ...,
        EndpointType: str = ...,
        IdentityProviderDetails: "Server.IdentityProviderDetails" = ...,
        IdentityProviderType: str = ...,
        LoggingRole: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class EndpointDetails:
        def __init__(
            self,
            *,
            AddressAllocationIds: List[str] = ...,
            SubnetIds: List[str] = ...,
            VpcEndpointId: str = ...,
            VpcId: str = ...
        ): ...
    class IdentityProviderDetails:
        def __init__(self, *, InvocationRole: str, Url: str): ...

class User:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html"""

    ServerId: Final[str]

    UserName: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Role: str,
        ServerId: str,
        UserName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        HomeDirectory: str = ...,
        HomeDirectoryMappings: List["User.HomeDirectoryMapEntry"] = ...,
        HomeDirectoryType: str = ...,
        Policy: str = ...,
        SshPublicKeys: List["User.SshPublicKey"] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class HomeDirectoryMapEntry:
        def __init__(self, *, Entry: str, Target: str): ...
    class SshPublicKey:
        def __init__(self) -> None: ...
