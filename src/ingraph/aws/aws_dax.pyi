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

_NAMESPACE = "AWS::DAX"

class Cluster:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-cluster.html"""

    ClusterDiscoveryEndpoint: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        IAMRoleARN: str,
        NodeType: str,
        ReplicationFactor: int,
        AvailabilityZones: List[str] = ...,
        ClusterName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        NotificationTopicARN: str = ...,
        ParameterGroupName: str = ...,
        PreferredMaintenanceWindow: str = ...,
        SSESpecification: "Cluster.SSESpecification" = ...,
        SecurityGroupIds: List[str] = ...,
        SubnetGroupName: str = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class SSESpecification:
        def __init__(self, *, SSEEnabled: bool = ...): ...

class ParameterGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-parametergroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        ParameterGroupName: str = ...,
        ParameterNameValues: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class SubnetGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dax-subnetgroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        SubnetIds: List[str],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        SubnetGroupName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
