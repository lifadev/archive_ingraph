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

_NAMESPACE = "AWS::ElasticLoadBalancingV2"

class Listener:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listener.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DefaultActions: List["Listener.Action"],
        LoadBalancerArn: str,
        Port: int,
        Protocol: str,
        Certificates: List["Listener.Certificate"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        SslPolicy: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Action:
        def __init__(
            self,
            *,
            Type: str,
            AuthenticateCognitoConfig: "Listener.AuthenticateCognitoConfig" = ...,
            AuthenticateOidcConfig: "Listener.AuthenticateOidcConfig" = ...,
            FixedResponseConfig: "Listener.FixedResponseConfig" = ...,
            ForwardConfig: "Listener.ForwardConfig" = ...,
            Order: int = ...,
            RedirectConfig: "Listener.RedirectConfig" = ...,
            TargetGroupArn: str = ...
        ): ...
    class AuthenticateCognitoConfig:
        def __init__(
            self,
            *,
            UserPoolArn: str,
            UserPoolClientId: str,
            UserPoolDomain: str,
            AuthenticationRequestExtraParams: Dict[str, str] = ...,
            OnUnauthenticatedRequest: str = ...,
            Scope: str = ...,
            SessionCookieName: str = ...,
            SessionTimeout: int = ...
        ): ...
    class AuthenticateOidcConfig:
        def __init__(
            self,
            *,
            AuthorizationEndpoint: str,
            ClientId: str,
            ClientSecret: str,
            Issuer: str,
            TokenEndpoint: str,
            UserInfoEndpoint: str,
            AuthenticationRequestExtraParams: Dict[str, str] = ...,
            OnUnauthenticatedRequest: str = ...,
            Scope: str = ...,
            SessionCookieName: str = ...,
            SessionTimeout: int = ...
        ): ...
    class Certificate:
        def __init__(self, *, CertificateArn: str = ...): ...
    class FixedResponseConfig:
        def __init__(
            self, *, StatusCode: str, ContentType: str = ..., MessageBody: str = ...
        ): ...
    class ForwardConfig:
        def __init__(
            self,
            *,
            TargetGroupStickinessConfig: "Listener.TargetGroupStickinessConfig" = ...,
            TargetGroups: List["Listener.TargetGroupTuple"] = ...
        ): ...
    class RedirectConfig:
        def __init__(
            self,
            *,
            StatusCode: str,
            Host: str = ...,
            Path: str = ...,
            Port: str = ...,
            Protocol: str = ...,
            Query: str = ...
        ): ...
    class TargetGroupStickinessConfig:
        def __init__(self, *, DurationSeconds: int = ..., Enabled: bool = ...): ...
    class TargetGroupTuple:
        def __init__(self, *, TargetGroupArn: str = ..., Weight: int = ...): ...

class ListenerCertificate:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenercertificate.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Certificates: List["ListenerCertificate.Certificate"],
        ListenerArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Certificate:
        def __init__(self, *, CertificateArn: str = ...): ...

class ListenerRule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-listenerrule.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Actions: List["ListenerRule.Action"],
        Conditions: List["ListenerRule.RuleCondition"],
        ListenerArn: str,
        Priority: int,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Action:
        def __init__(
            self,
            *,
            Type: str,
            AuthenticateCognitoConfig: "ListenerRule.AuthenticateCognitoConfig" = ...,
            AuthenticateOidcConfig: "ListenerRule.AuthenticateOidcConfig" = ...,
            FixedResponseConfig: "ListenerRule.FixedResponseConfig" = ...,
            ForwardConfig: "ListenerRule.ForwardConfig" = ...,
            Order: int = ...,
            RedirectConfig: "ListenerRule.RedirectConfig" = ...,
            TargetGroupArn: str = ...
        ): ...
    class AuthenticateCognitoConfig:
        def __init__(
            self,
            *,
            UserPoolArn: str,
            UserPoolClientId: str,
            UserPoolDomain: str,
            AuthenticationRequestExtraParams: Dict[str, str] = ...,
            OnUnauthenticatedRequest: str = ...,
            Scope: str = ...,
            SessionCookieName: str = ...,
            SessionTimeout: int = ...
        ): ...
    class AuthenticateOidcConfig:
        def __init__(
            self,
            *,
            AuthorizationEndpoint: str,
            ClientId: str,
            ClientSecret: str,
            Issuer: str,
            TokenEndpoint: str,
            UserInfoEndpoint: str,
            AuthenticationRequestExtraParams: Dict[str, str] = ...,
            OnUnauthenticatedRequest: str = ...,
            Scope: str = ...,
            SessionCookieName: str = ...,
            SessionTimeout: int = ...
        ): ...
    class FixedResponseConfig:
        def __init__(
            self, *, StatusCode: str, ContentType: str = ..., MessageBody: str = ...
        ): ...
    class ForwardConfig:
        def __init__(
            self,
            *,
            TargetGroupStickinessConfig: "ListenerRule.TargetGroupStickinessConfig" = ...,
            TargetGroups: List["ListenerRule.TargetGroupTuple"] = ...
        ): ...
    class HostHeaderConfig:
        def __init__(self, *, Values: List[str] = ...): ...
    class HttpHeaderConfig:
        def __init__(self, *, HttpHeaderName: str = ..., Values: List[str] = ...): ...
    class HttpRequestMethodConfig:
        def __init__(self, *, Values: List[str] = ...): ...
    class PathPatternConfig:
        def __init__(self, *, Values: List[str] = ...): ...
    class QueryStringConfig:
        def __init__(
            self, *, Values: List["ListenerRule.QueryStringKeyValue"] = ...
        ): ...
    class QueryStringKeyValue:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...
    class RedirectConfig:
        def __init__(
            self,
            *,
            StatusCode: str,
            Host: str = ...,
            Path: str = ...,
            Port: str = ...,
            Protocol: str = ...,
            Query: str = ...
        ): ...
    class RuleCondition:
        def __init__(
            self,
            *,
            Field: str = ...,
            HostHeaderConfig: "ListenerRule.HostHeaderConfig" = ...,
            HttpHeaderConfig: "ListenerRule.HttpHeaderConfig" = ...,
            HttpRequestMethodConfig: "ListenerRule.HttpRequestMethodConfig" = ...,
            PathPatternConfig: "ListenerRule.PathPatternConfig" = ...,
            QueryStringConfig: "ListenerRule.QueryStringConfig" = ...,
            SourceIpConfig: "ListenerRule.SourceIpConfig" = ...,
            Values: List[str] = ...
        ): ...
    class SourceIpConfig:
        def __init__(self, *, Values: List[str] = ...): ...
    class TargetGroupStickinessConfig:
        def __init__(self, *, DurationSeconds: int = ..., Enabled: bool = ...): ...
    class TargetGroupTuple:
        def __init__(self, *, TargetGroupArn: str = ..., Weight: int = ...): ...

class LoadBalancer:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html"""

    CanonicalHostedZoneID: Final[str]

    DNSName: Final[str]

    LoadBalancerFullName: Final[str]

    LoadBalancerName: Final[str]

    SecurityGroups: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        IpAddressType: str = ...,
        LoadBalancerAttributes: List["LoadBalancer.LoadBalancerAttribute"] = ...,
        Name: str = ...,
        Scheme: str = ...,
        SecurityGroups: List[str] = ...,
        SubnetMappings: List["LoadBalancer.SubnetMapping"] = ...,
        Subnets: List[str] = ...,
        Tags: List["Tag"] = ...,
        Type: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class LoadBalancerAttribute:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...
    class SubnetMapping:
        def __init__(self, *, AllocationId: str, SubnetId: str): ...

class TargetGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-targetgroup.html"""

    LoadBalancerArns: Final[List[str]]

    TargetGroupFullName: Final[str]

    TargetGroupName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        HealthCheckEnabled: bool = ...,
        HealthCheckIntervalSeconds: int = ...,
        HealthCheckPath: str = ...,
        HealthCheckPort: str = ...,
        HealthCheckProtocol: str = ...,
        HealthCheckTimeoutSeconds: int = ...,
        HealthyThresholdCount: int = ...,
        Matcher: "TargetGroup.Matcher" = ...,
        Name: str = ...,
        Port: int = ...,
        Protocol: str = ...,
        Tags: List["Tag"] = ...,
        TargetGroupAttributes: List["TargetGroup.TargetGroupAttribute"] = ...,
        TargetType: str = ...,
        Targets: List["TargetGroup.TargetDescription"] = ...,
        UnhealthyThresholdCount: int = ...,
        UpdateReplacePolicy: str = ...,
        VpcId: str = ...
    ): ...
    class Matcher:
        def __init__(self, *, HttpCode: str): ...
    class TargetDescription:
        def __init__(
            self, *, Id: str, AvailabilityZone: str = ..., Port: int = ...
        ): ...
    class TargetGroupAttribute:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...
