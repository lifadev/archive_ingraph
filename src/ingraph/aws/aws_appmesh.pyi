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

_NAMESPACE = "AWS::AppMesh"

class Mesh:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-mesh.html"""

    Uid: Final[str]

    MeshName: Final[str]

    MeshOwner: Final[str]

    ResourceOwner: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        MeshName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Spec: "Mesh.MeshSpec" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class EgressFilter:
        def __init__(self, *, Type: str): ...
    class MeshSpec:
        def __init__(self, *, EgressFilter: "Mesh.EgressFilter" = ...): ...

class Route:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-route.html"""

    Uid: Final[str]

    MeshName: Final[str]

    VirtualRouterName: Final[str]

    MeshOwner: Final[str]

    ResourceOwner: Final[str]

    RouteName: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        MeshName: str,
        RouteName: str,
        Spec: "Route.RouteSpec",
        VirtualRouterName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        MeshOwner: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Duration:
        def __init__(self, *, Unit: str, Value: int): ...
    class GrpcRetryPolicy:
        def __init__(
            self,
            *,
            MaxRetries: int,
            PerRetryTimeout: "Route.Duration",
            GrpcRetryEvents: List[str] = ...,
            HttpRetryEvents: List[str] = ...,
            TcpRetryEvents: List[str] = ...
        ): ...
    class GrpcRoute:
        def __init__(
            self,
            *,
            Action: "Route.GrpcRouteAction",
            Match: "Route.GrpcRouteMatch",
            RetryPolicy: "Route.GrpcRetryPolicy" = ...
        ): ...
    class GrpcRouteAction:
        def __init__(self, *, WeightedTargets: List["Route.WeightedTarget"]): ...
    class GrpcRouteMatch:
        def __init__(
            self,
            *,
            Metadata: List["Route.GrpcRouteMetadata"] = ...,
            MethodName: str = ...,
            ServiceName: str = ...
        ): ...
    class GrpcRouteMetadata:
        def __init__(
            self,
            *,
            Name: str,
            Invert: bool = ...,
            Match: "Route.GrpcRouteMetadataMatchMethod" = ...
        ): ...
    class GrpcRouteMetadataMatchMethod:
        def __init__(
            self,
            *,
            Exact: str = ...,
            Prefix: str = ...,
            Range: "Route.MatchRange" = ...,
            Regex: str = ...,
            Suffix: str = ...
        ): ...
    class HeaderMatchMethod:
        def __init__(
            self,
            *,
            Exact: str = ...,
            Prefix: str = ...,
            Range: "Route.MatchRange" = ...,
            Regex: str = ...,
            Suffix: str = ...
        ): ...
    class HttpRetryPolicy:
        def __init__(
            self,
            *,
            MaxRetries: int,
            PerRetryTimeout: "Route.Duration",
            HttpRetryEvents: List[str] = ...,
            TcpRetryEvents: List[str] = ...
        ): ...
    class HttpRoute:
        def __init__(
            self,
            *,
            Action: "Route.HttpRouteAction",
            Match: "Route.HttpRouteMatch",
            RetryPolicy: "Route.HttpRetryPolicy" = ...
        ): ...
    class HttpRouteAction:
        def __init__(self, *, WeightedTargets: List["Route.WeightedTarget"]): ...
    class HttpRouteHeader:
        def __init__(
            self,
            *,
            Name: str,
            Invert: bool = ...,
            Match: "Route.HeaderMatchMethod" = ...
        ): ...
    class HttpRouteMatch:
        def __init__(
            self,
            *,
            Prefix: str,
            Headers: List["Route.HttpRouteHeader"] = ...,
            Method: str = ...,
            Scheme: str = ...
        ): ...
    class MatchRange:
        def __init__(self, *, End: int, Start: int): ...
    class RouteSpec:
        def __init__(
            self,
            *,
            GrpcRoute: "Route.GrpcRoute" = ...,
            Http2Route: "Route.HttpRoute" = ...,
            HttpRoute: "Route.HttpRoute" = ...,
            Priority: int = ...,
            TcpRoute: "Route.TcpRoute" = ...
        ): ...
    class TcpRoute:
        def __init__(self, *, Action: "Route.TcpRouteAction"): ...
    class TcpRouteAction:
        def __init__(self, *, WeightedTargets: List["Route.WeightedTarget"]): ...
    class WeightedTarget:
        def __init__(self, *, VirtualNode: str, Weight: int): ...

class VirtualNode:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualnode.html"""

    Uid: Final[str]

    MeshName: Final[str]

    MeshOwner: Final[str]

    ResourceOwner: Final[str]

    Arn: Final[str]

    VirtualNodeName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        MeshName: str,
        Spec: "VirtualNode.VirtualNodeSpec",
        VirtualNodeName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        MeshOwner: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AccessLog:
        def __init__(self, *, File: "VirtualNode.FileAccessLog" = ...): ...
    class AwsCloudMapInstanceAttribute:
        def __init__(self, *, Key: str, Value: str): ...
    class AwsCloudMapServiceDiscovery:
        def __init__(
            self,
            *,
            NamespaceName: str,
            ServiceName: str,
            Attributes: List["VirtualNode.AwsCloudMapInstanceAttribute"] = ...
        ): ...
    class Backend:
        def __init__(
            self, *, VirtualService: "VirtualNode.VirtualServiceBackend" = ...
        ): ...
    class BackendDefaults:
        def __init__(self, *, ClientPolicy: "VirtualNode.ClientPolicy" = ...): ...
    class ClientPolicy:
        def __init__(self, *, TLS: "VirtualNode.ClientPolicyTls" = ...): ...
    class ClientPolicyTls:
        def __init__(
            self,
            *,
            Validation: "VirtualNode.TlsValidationContext",
            Enforce: bool = ...,
            Ports: List[int] = ...
        ): ...
    class DnsServiceDiscovery:
        def __init__(self, *, Hostname: str): ...
    class FileAccessLog:
        def __init__(self, *, Path: str): ...
    class HealthCheck:
        def __init__(
            self,
            *,
            HealthyThreshold: int,
            IntervalMillis: int,
            Protocol: str,
            TimeoutMillis: int,
            UnhealthyThreshold: int,
            Path: str = ...,
            Port: int = ...
        ): ...
    class Listener:
        def __init__(
            self,
            *,
            PortMapping: "VirtualNode.PortMapping",
            HealthCheck: "VirtualNode.HealthCheck" = ...,
            TLS: "VirtualNode.ListenerTls" = ...
        ): ...
    class ListenerTls:
        def __init__(
            self, *, Certificate: "VirtualNode.ListenerTlsCertificate", Mode: str
        ): ...
    class ListenerTlsAcmCertificate:
        def __init__(self, *, CertificateArn: str): ...
    class ListenerTlsCertificate:
        def __init__(
            self,
            *,
            ACM: "VirtualNode.ListenerTlsAcmCertificate" = ...,
            File: "VirtualNode.ListenerTlsFileCertificate" = ...
        ): ...
    class ListenerTlsFileCertificate:
        def __init__(self, *, CertificateChain: str, PrivateKey: str): ...
    class Logging:
        def __init__(self, *, AccessLog: "VirtualNode.AccessLog" = ...): ...
    class PortMapping:
        def __init__(self, *, Port: int, Protocol: str): ...
    class ServiceDiscovery:
        def __init__(
            self,
            *,
            AWSCloudMap: "VirtualNode.AwsCloudMapServiceDiscovery" = ...,
            DNS: "VirtualNode.DnsServiceDiscovery" = ...
        ): ...
    class TlsValidationContext:
        def __init__(self, *, Trust: "VirtualNode.TlsValidationContextTrust"): ...
    class TlsValidationContextAcmTrust:
        def __init__(self, *, CertificateAuthorityArns: List[str]): ...
    class TlsValidationContextFileTrust:
        def __init__(self, *, CertificateChain: str): ...
    class TlsValidationContextTrust:
        def __init__(
            self,
            *,
            ACM: "VirtualNode.TlsValidationContextAcmTrust" = ...,
            File: "VirtualNode.TlsValidationContextFileTrust" = ...
        ): ...
    class VirtualNodeSpec:
        def __init__(
            self,
            *,
            BackendDefaults: "VirtualNode.BackendDefaults" = ...,
            Backends: List["VirtualNode.Backend"] = ...,
            Listeners: List["VirtualNode.Listener"] = ...,
            Logging: "VirtualNode.Logging" = ...,
            ServiceDiscovery: "VirtualNode.ServiceDiscovery" = ...
        ): ...
    class VirtualServiceBackend:
        def __init__(
            self,
            *,
            VirtualServiceName: str,
            ClientPolicy: "VirtualNode.ClientPolicy" = ...
        ): ...

class VirtualRouter:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualrouter.html"""

    Uid: Final[str]

    MeshName: Final[str]

    VirtualRouterName: Final[str]

    MeshOwner: Final[str]

    ResourceOwner: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        MeshName: str,
        Spec: "VirtualRouter.VirtualRouterSpec",
        VirtualRouterName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        MeshOwner: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class PortMapping:
        def __init__(self, *, Port: int, Protocol: str): ...
    class VirtualRouterListener:
        def __init__(self, *, PortMapping: "VirtualRouter.PortMapping"): ...
    class VirtualRouterSpec:
        def __init__(
            self, *, Listeners: List["VirtualRouter.VirtualRouterListener"]
        ): ...

class VirtualService:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appmesh-virtualservice.html"""

    Uid: Final[str]

    MeshName: Final[str]

    MeshOwner: Final[str]

    ResourceOwner: Final[str]

    VirtualServiceName: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        MeshName: str,
        Spec: "VirtualService.VirtualServiceSpec",
        VirtualServiceName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        MeshOwner: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class VirtualNodeServiceProvider:
        def __init__(self, *, VirtualNodeName: str): ...
    class VirtualRouterServiceProvider:
        def __init__(self, *, VirtualRouterName: str): ...
    class VirtualServiceProvider:
        def __init__(
            self,
            *,
            VirtualNode: "VirtualService.VirtualNodeServiceProvider" = ...,
            VirtualRouter: "VirtualService.VirtualRouterServiceProvider" = ...
        ): ...
    class VirtualServiceSpec:
        def __init__(
            self, *, Provider: "VirtualService.VirtualServiceProvider" = ...
        ): ...
