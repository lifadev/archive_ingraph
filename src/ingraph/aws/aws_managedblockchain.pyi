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

_NAMESPACE = "AWS::ManagedBlockchain"

class Member:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-member.html"""

    MemberId: Final[str]

    NetworkId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        MemberConfiguration: "Member.MemberConfiguration",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InvitationId: str = ...,
        NetworkConfiguration: "Member.NetworkConfiguration" = ...,
        NetworkId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ApprovalThresholdPolicy:
        def __init__(
            self,
            *,
            ProposalDurationInHours: int = ...,
            ThresholdComparator: str = ...,
            ThresholdPercentage: int = ...
        ): ...
    class MemberConfiguration:
        def __init__(
            self,
            *,
            Name: str,
            Description: str = ...,
            MemberFrameworkConfiguration: "Member.MemberFrameworkConfiguration" = ...
        ): ...
    class MemberFabricConfiguration:
        def __init__(self, *, AdminPassword: str, AdminUsername: str): ...
    class MemberFrameworkConfiguration:
        def __init__(
            self, *, MemberFabricConfiguration: "Member.MemberFabricConfiguration" = ...
        ): ...
    class NetworkConfiguration:
        def __init__(
            self,
            *,
            Framework: str,
            FrameworkVersion: str,
            Name: str,
            VotingPolicy: "Member.VotingPolicy",
            Description: str = ...,
            NetworkFrameworkConfiguration: "Member.NetworkFrameworkConfiguration" = ...
        ): ...
    class NetworkFabricConfiguration:
        def __init__(self, *, Edition: str): ...
    class NetworkFrameworkConfiguration:
        def __init__(
            self,
            *,
            NetworkFabricConfiguration: "Member.NetworkFabricConfiguration" = ...
        ): ...
    class VotingPolicy:
        def __init__(
            self, *, ApprovalThresholdPolicy: "Member.ApprovalThresholdPolicy" = ...
        ): ...

class Node:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-managedblockchain-node.html"""

    MemberId: Final[str]

    NodeId: Final[str]

    Arn: Final[str]

    NetworkId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        MemberId: str,
        NetworkId: str,
        NodeConfiguration: "Node.NodeConfiguration",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class NodeConfiguration:
        def __init__(self, *, AvailabilityZone: str, InstanceType: str): ...
