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

_NAMESPACE = "AWS::ElasticLoadBalancing"

class LoadBalancer:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html"""

    CanonicalHostedZoneName: Final[str]

    CanonicalHostedZoneNameID: Final[str]

    DNSName: Final[str]

    SourceSecurityGroup_GroupName: Final[str]

    SourceSecurityGroup_OwnerAlias: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Listeners: List["LoadBalancer.Listeners"],
        AccessLoggingPolicy: "LoadBalancer.AccessLoggingPolicy" = ...,
        AppCookieStickinessPolicy: List["LoadBalancer.AppCookieStickinessPolicy"] = ...,
        AvailabilityZones: List[str] = ...,
        ConnectionDrainingPolicy: "LoadBalancer.ConnectionDrainingPolicy" = ...,
        ConnectionSettings: "LoadBalancer.ConnectionSettings" = ...,
        CrossZone: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        HealthCheck: "LoadBalancer.HealthCheck" = ...,
        Instances: List[str] = ...,
        LBCookieStickinessPolicy: List["LoadBalancer.LBCookieStickinessPolicy"] = ...,
        LoadBalancerName: str = ...,
        Policies: List["LoadBalancer.Policies"] = ...,
        Scheme: str = ...,
        SecurityGroups: List[str] = ...,
        Subnets: List[str] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AccessLoggingPolicy:
        def __init__(
            self,
            *,
            Enabled: bool,
            S3BucketName: str,
            EmitInterval: int = ...,
            S3BucketPrefix: str = ...
        ): ...
    class AppCookieStickinessPolicy:
        def __init__(self, *, CookieName: str, PolicyName: str): ...
    class ConnectionDrainingPolicy:
        def __init__(self, *, Enabled: bool, Timeout: int = ...): ...
    class ConnectionSettings:
        def __init__(self, *, IdleTimeout: int): ...
    class HealthCheck:
        def __init__(
            self,
            *,
            HealthyThreshold: str,
            Interval: str,
            Target: str,
            Timeout: str,
            UnhealthyThreshold: str
        ): ...
    class LBCookieStickinessPolicy:
        def __init__(
            self, *, CookieExpirationPeriod: str = ..., PolicyName: str = ...
        ): ...
    class Listeners:
        def __init__(
            self,
            *,
            InstancePort: str,
            LoadBalancerPort: str,
            Protocol: str,
            InstanceProtocol: str = ...,
            PolicyNames: List[str] = ...,
            SSLCertificateId: str = ...
        ): ...
    class Policies:
        def __init__(
            self,
            *,
            Attributes: List[Any],
            PolicyName: str,
            PolicyType: str,
            InstancePorts: List[str] = ...,
            LoadBalancerPorts: List[str] = ...
        ): ...
