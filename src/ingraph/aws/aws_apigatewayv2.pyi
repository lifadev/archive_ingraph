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

_NAMESPACE = "AWS::ApiGatewayV2"

class Api:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiKeySelectionExpression: str = ...,
        BasePath: str = ...,
        Body: Any = ...,
        BodyS3Location: "Api.BodyS3Location" = ...,
        CorsConfiguration: "Api.Cors" = ...,
        CredentialsArn: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        DisableSchemaValidation: bool = ...,
        FailOnWarnings: bool = ...,
        Name: str = ...,
        ProtocolType: str = ...,
        RouteKey: str = ...,
        RouteSelectionExpression: str = ...,
        Tags: Any = ...,
        Target: str = ...,
        UpdateReplacePolicy: str = ...,
        Version: str = ...
    ): ...
    class BodyS3Location:
        def __init__(
            self,
            *,
            Bucket: str = ...,
            Etag: str = ...,
            Key: str = ...,
            Version: str = ...
        ): ...
    class Cors:
        def __init__(
            self,
            *,
            AllowCredentials: bool = ...,
            AllowHeaders: List[str] = ...,
            AllowMethods: List[str] = ...,
            AllowOrigins: List[str] = ...,
            ExposeHeaders: List[str] = ...,
            MaxAge: int = ...
        ): ...

class ApiMapping:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        DomainName: str,
        Stage: str,
        ApiMappingKey: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Authorizer:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        AuthorizerType: str,
        IdentitySource: List[str],
        Name: str,
        AuthorizerCredentialsArn: str = ...,
        AuthorizerResultTtlInSeconds: int = ...,
        AuthorizerUri: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        IdentityValidationExpression: str = ...,
        JwtConfiguration: "Authorizer.JWTConfiguration" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class JWTConfiguration:
        def __init__(self, *, Audience: List[str] = ..., Issuer: str = ...): ...

class Deployment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        StageName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class DomainName:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html"""

    RegionalHostedZoneId: Final[str]

    RegionalDomainName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DomainName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DomainNameConfigurations: List["DomainName.DomainNameConfiguration"] = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DomainNameConfiguration:
        def __init__(
            self,
            *,
            CertificateArn: str = ...,
            CertificateName: str = ...,
            EndpointType: str = ...
        ): ...

class Integration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        IntegrationType: str,
        ConnectionId: str = ...,
        ConnectionType: str = ...,
        ContentHandlingStrategy: str = ...,
        CredentialsArn: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        IntegrationMethod: str = ...,
        IntegrationUri: str = ...,
        PassthroughBehavior: str = ...,
        PayloadFormatVersion: str = ...,
        RequestParameters: Any = ...,
        RequestTemplates: Any = ...,
        TemplateSelectionExpression: str = ...,
        TimeoutInMillis: int = ...,
        TlsConfig: "Integration.TlsConfig" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class TlsConfig:
        def __init__(self, *, ServerNameToVerify: str = ...): ...

class IntegrationResponse:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        IntegrationId: str,
        IntegrationResponseKey: str,
        ContentHandlingStrategy: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ResponseParameters: Any = ...,
        ResponseTemplates: Any = ...,
        TemplateSelectionExpression: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Model:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        Name: str,
        Schema: Any,
        ContentType: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Route:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        RouteKey: str,
        ApiKeyRequired: bool = ...,
        AuthorizationScopes: List[str] = ...,
        AuthorizationType: str = ...,
        AuthorizerId: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ModelSelectionExpression: str = ...,
        OperationName: str = ...,
        RequestModels: Any = ...,
        RequestParameters: Any = ...,
        RouteResponseSelectionExpression: str = ...,
        Target: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ParameterConstraints:
        def __init__(self, *, Required: bool): ...

class RouteResponse:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        RouteId: str,
        RouteResponseKey: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ModelSelectionExpression: str = ...,
        ResponseModels: Any = ...,
        ResponseParameters: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ParameterConstraints:
        def __init__(self, *, Required: bool): ...

class Stage:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        StageName: str,
        AccessLogSettings: "Stage.AccessLogSettings" = ...,
        AutoDeploy: bool = ...,
        ClientCertificateId: str = ...,
        DefaultRouteSettings: "Stage.RouteSettings" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DeploymentId: str = ...,
        Description: str = ...,
        RouteSettings: Any = ...,
        StageVariables: Any = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AccessLogSettings:
        def __init__(self, *, DestinationArn: str = ..., Format: str = ...): ...
    class RouteSettings:
        def __init__(
            self,
            *,
            DataTraceEnabled: bool = ...,
            DetailedMetricsEnabled: bool = ...,
            LoggingLevel: str = ...,
            ThrottlingBurstLimit: int = ...,
            ThrottlingRateLimit: float = ...
        ): ...
