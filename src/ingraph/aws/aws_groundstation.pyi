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

_NAMESPACE = "AWS::GroundStation"

class Config:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.html"""

    Type: Final[str]

    Arn: Final[str]

    Id: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ConfigData: Any,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class DataflowEndpointGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-dataflowendpointgroup.html"""

    Id: Final[str]

    Arn: Final[str]

    Status: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        EndpointDetails: List["DataflowEndpointGroup.EndpointDetails"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DataflowEndpoint:
        def __init__(
            self,
            *,
            Address: "DataflowEndpointGroup.SocketAddress" = ...,
            Name: str = ...
        ): ...
    class EndpointDetails:
        def __init__(
            self,
            *,
            Endpoint: "DataflowEndpointGroup.DataflowEndpoint" = ...,
            SecurityDetails: "DataflowEndpointGroup.SecurityDetails" = ...
        ): ...
    class SecurityDetails:
        def __init__(
            self,
            *,
            RoleArn: str = ...,
            SecurityGroupIds: List[str] = ...,
            SubnetIds: List[str] = ...
        ): ...
    class SocketAddress:
        def __init__(self, *, Name: str = ..., Port: int = ...): ...

class MissionProfile:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html"""

    Id: Final[str]

    Arn: Final[str]

    Region: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DataflowEdges: List["MissionProfile.DataflowEdge"],
        MinimumViableContactDurationSeconds: int,
        Name: str,
        TrackingConfigArn: str,
        ContactPostPassDurationSeconds: int = ...,
        ContactPrePassDurationSeconds: int = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DataflowEdge:
        def __init__(self, *, Destination: str = ..., Source: str = ...): ...
