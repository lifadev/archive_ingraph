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

_NAMESPACE = "AWS::ApiGateway"

class Account:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-account.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CloudWatchRoleArn: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ApiKey:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-apikey.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CustomerId: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Enabled: bool = ...,
        GenerateDistinctId: bool = ...,
        Name: str = ...,
        StageKeys: List["ApiKey.StageKey"] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        Value: str = ...
    ): ...
    class StageKey:
        def __init__(self, *, RestApiId: str = ..., StageName: str = ...): ...

class Authorizer:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-authorizer.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        RestApiId: str,
        Type: str,
        AuthType: str = ...,
        AuthorizerCredentials: str = ...,
        AuthorizerResultTtlInSeconds: int = ...,
        AuthorizerUri: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        IdentitySource: str = ...,
        IdentityValidationExpression: str = ...,
        Name: str = ...,
        ProviderARNs: List[str] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class BasePathMapping:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-basepathmapping.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DomainName: str,
        BasePath: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RestApiId: str = ...,
        Stage: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ClientCertificate:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-clientcertificate.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Deployment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-deployment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        RestApiId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DeploymentCanarySettings: "Deployment.DeploymentCanarySettings" = ...,
        Description: str = ...,
        StageDescription: "Deployment.StageDescription" = ...,
        StageName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AccessLogSetting:
        def __init__(self, *, DestinationArn: str = ..., Format: str = ...): ...
    class CanarySetting:
        def __init__(
            self,
            *,
            PercentTraffic: float = ...,
            StageVariableOverrides: Dict[str, str] = ...,
            UseStageCache: bool = ...
        ): ...
    class DeploymentCanarySettings:
        def __init__(
            self,
            *,
            PercentTraffic: float = ...,
            StageVariableOverrides: Dict[str, str] = ...,
            UseStageCache: bool = ...
        ): ...
    class MethodSetting:
        def __init__(
            self,
            *,
            CacheDataEncrypted: bool = ...,
            CacheTtlInSeconds: int = ...,
            CachingEnabled: bool = ...,
            DataTraceEnabled: bool = ...,
            HttpMethod: str = ...,
            LoggingLevel: str = ...,
            MetricsEnabled: bool = ...,
            ResourcePath: str = ...,
            ThrottlingBurstLimit: int = ...,
            ThrottlingRateLimit: float = ...
        ): ...
    class StageDescription:
        def __init__(
            self,
            *,
            AccessLogSetting: "Deployment.AccessLogSetting" = ...,
            CacheClusterEnabled: bool = ...,
            CacheClusterSize: str = ...,
            CacheDataEncrypted: bool = ...,
            CacheTtlInSeconds: int = ...,
            CachingEnabled: bool = ...,
            CanarySetting: "Deployment.CanarySetting" = ...,
            ClientCertificateId: str = ...,
            DataTraceEnabled: bool = ...,
            Description: str = ...,
            DocumentationVersion: str = ...,
            LoggingLevel: str = ...,
            MethodSettings: List["Deployment.MethodSetting"] = ...,
            MetricsEnabled: bool = ...,
            Tags: List["Tag"] = ...,
            ThrottlingBurstLimit: int = ...,
            ThrottlingRateLimit: float = ...,
            TracingEnabled: bool = ...,
            Variables: Dict[str, str] = ...
        ): ...

class DocumentationPart:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationpart.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Location: "DocumentationPart.Location",
        Properties: str,
        RestApiId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Location:
        def __init__(
            self,
            *,
            Method: str = ...,
            Name: str = ...,
            Path: str = ...,
            StatusCode: str = ...,
            Type: str = ...
        ): ...

class DocumentationVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-documentationversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DocumentationVersion: str,
        RestApiId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class DomainName:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-domainname.html"""

    DistributionDomainName: Final[str]

    DistributionHostedZoneId: Final[str]

    RegionalDomainName: Final[str]

    RegionalHostedZoneId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DomainName: str,
        CertificateArn: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EndpointConfiguration: "DomainName.EndpointConfiguration" = ...,
        RegionalCertificateArn: str = ...,
        SecurityPolicy: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class EndpointConfiguration:
        def __init__(self, *, Types: List[str] = ...): ...

class GatewayResponse:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-gatewayresponse.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ResponseType: str,
        RestApiId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ResponseParameters: Dict[str, str] = ...,
        ResponseTemplates: Dict[str, str] = ...,
        StatusCode: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Method:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-method.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        HttpMethod: str,
        ResourceId: str,
        RestApiId: str,
        ApiKeyRequired: bool = ...,
        AuthorizationScopes: List[str] = ...,
        AuthorizationType: str = ...,
        AuthorizerId: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Integration: "Method.Integration" = ...,
        MethodResponses: List["Method.MethodResponse"] = ...,
        OperationName: str = ...,
        RequestModels: Dict[str, str] = ...,
        RequestParameters: Dict[str, bool] = ...,
        RequestValidatorId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Integration:
        def __init__(
            self,
            *,
            CacheKeyParameters: List[str] = ...,
            CacheNamespace: str = ...,
            ConnectionId: str = ...,
            ConnectionType: str = ...,
            ContentHandling: str = ...,
            Credentials: str = ...,
            IntegrationHttpMethod: str = ...,
            IntegrationResponses: List["Method.IntegrationResponse"] = ...,
            PassthroughBehavior: str = ...,
            RequestParameters: Dict[str, str] = ...,
            RequestTemplates: Dict[str, str] = ...,
            TimeoutInMillis: int = ...,
            Type: str = ...,
            Uri: str = ...
        ): ...
    class IntegrationResponse:
        def __init__(
            self,
            *,
            StatusCode: str,
            ContentHandling: str = ...,
            ResponseParameters: Dict[str, str] = ...,
            ResponseTemplates: Dict[str, str] = ...,
            SelectionPattern: str = ...
        ): ...
    class MethodResponse:
        def __init__(
            self,
            *,
            StatusCode: str,
            ResponseModels: Dict[str, str] = ...,
            ResponseParameters: Dict[str, bool] = ...
        ): ...

class Model:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-model.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        RestApiId: str,
        ContentType: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Name: str = ...,
        Schema: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class RequestValidator:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-requestvalidator.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        RestApiId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        UpdateReplacePolicy: str = ...,
        ValidateRequestBody: bool = ...,
        ValidateRequestParameters: bool = ...
    ): ...

class Resource:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-resource.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ParentId: str,
        PathPart: str,
        RestApiId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class RestApi:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-restapi.html"""

    RootResourceId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiKeySourceType: str = ...,
        BinaryMediaTypes: List[str] = ...,
        Body: Any = ...,
        BodyS3Location: "RestApi.S3Location" = ...,
        CloneFrom: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        EndpointConfiguration: "RestApi.EndpointConfiguration" = ...,
        FailOnWarnings: bool = ...,
        MinimumCompressionSize: int = ...,
        Name: str = ...,
        Parameters: Dict[str, str] = ...,
        Policy: Any = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class EndpointConfiguration:
        def __init__(
            self, *, Types: List[str] = ..., VpcEndpointIds: List[str] = ...
        ): ...
    class S3Location:
        def __init__(
            self,
            *,
            Bucket: str = ...,
            ETag: str = ...,
            Key: str = ...,
            Version: str = ...
        ): ...

class Stage:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-stage.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        RestApiId: str,
        AccessLogSetting: "Stage.AccessLogSetting" = ...,
        CacheClusterEnabled: bool = ...,
        CacheClusterSize: str = ...,
        CanarySetting: "Stage.CanarySetting" = ...,
        ClientCertificateId: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DeploymentId: str = ...,
        Description: str = ...,
        DocumentationVersion: str = ...,
        MethodSettings: List["Stage.MethodSetting"] = ...,
        StageName: str = ...,
        Tags: List["Tag"] = ...,
        TracingEnabled: bool = ...,
        UpdateReplacePolicy: str = ...,
        Variables: Dict[str, str] = ...
    ): ...
    class AccessLogSetting:
        def __init__(self, *, DestinationArn: str = ..., Format: str = ...): ...
    class CanarySetting:
        def __init__(
            self,
            *,
            DeploymentId: str = ...,
            PercentTraffic: float = ...,
            StageVariableOverrides: Dict[str, str] = ...,
            UseStageCache: bool = ...
        ): ...
    class MethodSetting:
        def __init__(
            self,
            *,
            CacheDataEncrypted: bool = ...,
            CacheTtlInSeconds: int = ...,
            CachingEnabled: bool = ...,
            DataTraceEnabled: bool = ...,
            HttpMethod: str = ...,
            LoggingLevel: str = ...,
            MetricsEnabled: bool = ...,
            ResourcePath: str = ...,
            ThrottlingBurstLimit: int = ...,
            ThrottlingRateLimit: float = ...
        ): ...

class UsagePlan:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplan.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiStages: List["UsagePlan.ApiStage"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Quota: "UsagePlan.QuotaSettings" = ...,
        Tags: List["Tag"] = ...,
        Throttle: "UsagePlan.ThrottleSettings" = ...,
        UpdateReplacePolicy: str = ...,
        UsagePlanName: str = ...
    ): ...
    class ApiStage:
        def __init__(
            self,
            *,
            ApiId: str = ...,
            Stage: str = ...,
            Throttle: Dict[str, "UsagePlan.ThrottleSettings"] = ...
        ): ...
    class QuotaSettings:
        def __init__(
            self, *, Limit: int = ..., Offset: int = ..., Period: str = ...
        ): ...
    class ThrottleSettings:
        def __init__(self, *, BurstLimit: int = ..., RateLimit: float = ...): ...

class UsagePlanKey:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-usageplankey.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        KeyId: str,
        KeyType: str,
        UsagePlanId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class VpcLink:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-vpclink.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        TargetArns: List[str],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
