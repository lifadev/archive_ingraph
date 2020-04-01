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

_NAMESPACE = "AWS::AppSync"

class ApiCache:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apicache.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiCachingBehavior: str,
        ApiId: str,
        Ttl: float,
        Type: str,
        AtRestEncryptionEnabled: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        TransitEncryptionEnabled: bool = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ApiKey:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-apikey.html"""

    ApiKey_: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Expires: float = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class DataSource:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-datasource.html"""

    DataSourceArn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        Name: str,
        Type: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        DynamoDBConfig: "DataSource.DynamoDBConfig" = ...,
        ElasticsearchConfig: "DataSource.ElasticsearchConfig" = ...,
        HttpConfig: "DataSource.HttpConfig" = ...,
        LambdaConfig: "DataSource.LambdaConfig" = ...,
        RelationalDatabaseConfig: "DataSource.RelationalDatabaseConfig" = ...,
        ServiceRoleArn: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AuthorizationConfig:
        def __init__(
            self,
            *,
            AuthorizationType: str,
            AwsIamConfig: "DataSource.AwsIamConfig" = ...
        ): ...
    class AwsIamConfig:
        def __init__(
            self, *, SigningRegion: str = ..., SigningServiceName: str = ...
        ): ...
    class DeltaSyncConfig:
        def __init__(
            self, *, BaseTableTTL: str, DeltaSyncTableName: str, DeltaSyncTableTTL: str
        ): ...
    class DynamoDBConfig:
        def __init__(
            self,
            *,
            AwsRegion: str,
            TableName: str,
            DeltaSyncConfig: "DataSource.DeltaSyncConfig" = ...,
            UseCallerCredentials: bool = ...,
            Versioned: bool = ...
        ): ...
    class ElasticsearchConfig:
        def __init__(self, *, AwsRegion: str, Endpoint: str): ...
    class HttpConfig:
        def __init__(
            self,
            *,
            Endpoint: str,
            AuthorizationConfig: "DataSource.AuthorizationConfig" = ...
        ): ...
    class LambdaConfig:
        def __init__(self, *, LambdaFunctionArn: str): ...
    class RdsHttpEndpointConfig:
        def __init__(
            self,
            *,
            AwsRegion: str,
            AwsSecretStoreArn: str,
            DbClusterIdentifier: str,
            DatabaseName: str = ...,
            Schema: str = ...
        ): ...
    class RelationalDatabaseConfig:
        def __init__(
            self,
            *,
            RelationalDatabaseSourceType: str,
            RdsHttpEndpointConfig: "DataSource.RdsHttpEndpointConfig" = ...
        ): ...

class FunctionConfiguration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-functionconfiguration.html"""

    FunctionId: Final[str]

    FunctionArn: Final[str]

    DataSourceName: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        DataSourceName: str,
        FunctionVersion: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        RequestMappingTemplate: str = ...,
        RequestMappingTemplateS3Location: str = ...,
        ResponseMappingTemplate: str = ...,
        ResponseMappingTemplateS3Location: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class GraphQLApi:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlapi.html"""

    GraphQLUrl: Final[str]

    Arn: Final[str]

    ApiId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AuthenticationType: str,
        Name: str,
        AdditionalAuthenticationProviders: "GraphQLApi.AdditionalAuthenticationProviders" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        LogConfig: "GraphQLApi.LogConfig" = ...,
        OpenIDConnectConfig: "GraphQLApi.OpenIDConnectConfig" = ...,
        Tags: "GraphQLApi.Tags" = ...,
        UpdateReplacePolicy: str = ...,
        UserPoolConfig: "GraphQLApi.UserPoolConfig" = ...,
        XrayEnabled: bool = ...
    ): ...
    class AdditionalAuthenticationProvider:
        def __init__(
            self,
            *,
            AuthenticationType: str,
            OpenIDConnectConfig: "GraphQLApi.OpenIDConnectConfig" = ...,
            UserPoolConfig: "GraphQLApi.CognitoUserPoolConfig" = ...
        ): ...
    class AdditionalAuthenticationProviders:
        def __init__(self) -> None: ...
    class CognitoUserPoolConfig:
        def __init__(
            self,
            *,
            AppIdClientRegex: str = ...,
            AwsRegion: str = ...,
            UserPoolId: str = ...
        ): ...
    class LogConfig:
        def __init__(
            self,
            *,
            CloudWatchLogsRoleArn: str = ...,
            ExcludeVerboseContent: bool = ...,
            FieldLogLevel: str = ...
        ): ...
    class OpenIDConnectConfig:
        def __init__(
            self,
            *,
            AuthTTL: float = ...,
            ClientId: str = ...,
            IatTTL: float = ...,
            Issuer: str = ...
        ): ...
    class Tags:
        def __init__(self) -> None: ...
    class UserPoolConfig:
        def __init__(
            self,
            *,
            AppIdClientRegex: str = ...,
            AwsRegion: str = ...,
            DefaultAction: str = ...,
            UserPoolId: str = ...
        ): ...

class GraphQLSchema:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-graphqlschema.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        Definition: str = ...,
        DefinitionS3Location: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Resolver:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-resolver.html"""

    TypeName: Final[str]

    ResolverArn: Final[str]

    FieldName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ApiId: str,
        FieldName: str,
        TypeName: str,
        CachingConfig: "Resolver.CachingConfig" = ...,
        DataSourceName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Kind: str = ...,
        PipelineConfig: "Resolver.PipelineConfig" = ...,
        RequestMappingTemplate: str = ...,
        RequestMappingTemplateS3Location: str = ...,
        ResponseMappingTemplate: str = ...,
        ResponseMappingTemplateS3Location: str = ...,
        SyncConfig: "Resolver.SyncConfig" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CachingConfig:
        def __init__(self, *, CachingKeys: List[str] = ..., Ttl: float = ...): ...
    class LambdaConflictHandlerConfig:
        def __init__(self, *, LambdaConflictHandlerArn: str = ...): ...
    class PipelineConfig:
        def __init__(self, *, Functions: List[str] = ...): ...
    class SyncConfig:
        def __init__(
            self,
            *,
            ConflictDetection: str,
            ConflictHandler: str = ...,
            LambdaConflictHandlerConfig: "Resolver.LambdaConflictHandlerConfig" = ...
        ): ...
