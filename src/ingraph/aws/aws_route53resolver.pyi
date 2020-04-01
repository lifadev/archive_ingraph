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

_NAMESPACE = "AWS::Route53Resolver"

class ResolverEndpoint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverendpoint.html"""

    ResolverEndpointId: Final[str]

    IpAddressCount: Final[str]

    Arn: Final[str]

    Direction: Final[str]

    HostVPCId: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Direction: str,
        IpAddresses: List["ResolverEndpoint.IpAddressRequest"],
        SecurityGroupIds: List[str],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class IpAddressRequest:
        def __init__(self, *, SubnetId: str, Ip: str = ...): ...

class ResolverRule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverrule.html"""

    ResolverEndpointId: Final[str]

    DomainName: Final[str]

    ResolverRuleId: Final[str]

    Arn: Final[str]

    TargetIps: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DomainName: str,
        RuleType: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        ResolverEndpointId: str = ...,
        Tags: List["Tag"] = ...,
        TargetIps: List["ResolverRule.TargetAddress"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class TargetAddress:
        def __init__(self, *, Ip: str, Port: str = ...): ...

class ResolverRuleAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53resolver-resolverruleassociation.html"""

    VPCId: Final[str]

    ResolverRuleId: Final[str]

    ResolverRuleAssociationId: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ResolverRuleId: str,
        VPCId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
