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

_NAMESPACE = "AWS::Cognito"

class IdentityPool:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html"""

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AllowUnauthenticatedIdentities: bool,
        AllowClassicFlow: bool = ...,
        CognitoEvents: Any = ...,
        CognitoIdentityProviders: List["IdentityPool.CognitoIdentityProvider"] = ...,
        CognitoStreams: "IdentityPool.CognitoStreams" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DeveloperProviderName: str = ...,
        IdentityPoolName: str = ...,
        OpenIdConnectProviderARNs: List[str] = ...,
        PushSync: "IdentityPool.PushSync" = ...,
        SamlProviderARNs: List[str] = ...,
        SupportedLoginProviders: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CognitoIdentityProvider:
        def __init__(
            self,
            *,
            ClientId: str = ...,
            ProviderName: str = ...,
            ServerSideTokenCheck: bool = ...
        ): ...
    class CognitoStreams:
        def __init__(
            self,
            *,
            RoleArn: str = ...,
            StreamName: str = ...,
            StreamingStatus: str = ...
        ): ...
    class PushSync:
        def __init__(self, *, ApplicationArns: List[str] = ..., RoleArn: str = ...): ...

class IdentityPoolRoleAttachment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypoolroleattachment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        IdentityPoolId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RoleMappings: Any = ...,
        Roles: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class MappingRule:
        def __init__(self, *, Claim: str, MatchType: str, RoleARN: str, Value: str): ...
    class RoleMapping:
        def __init__(
            self,
            *,
            Type: str,
            AmbiguousRoleResolution: str = ...,
            IdentityProvider: str = ...,
            RulesConfiguration: "IdentityPoolRoleAttachment.RulesConfigurationType" = ...
        ): ...
    class RulesConfigurationType:
        def __init__(
            self, *, Rules: List["IdentityPoolRoleAttachment.MappingRule"]
        ): ...

class UserPool:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpool.html"""

    ProviderName: Final[str]

    ProviderURL: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AccountRecoverySetting: "UserPool.AccountRecoverySetting" = ...,
        AdminCreateUserConfig: "UserPool.AdminCreateUserConfig" = ...,
        AliasAttributes: List[str] = ...,
        AutoVerifiedAttributes: List[str] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DeviceConfiguration: "UserPool.DeviceConfiguration" = ...,
        EmailConfiguration: "UserPool.EmailConfiguration" = ...,
        EmailVerificationMessage: str = ...,
        EmailVerificationSubject: str = ...,
        EnabledMfas: List[str] = ...,
        LambdaConfig: "UserPool.LambdaConfig" = ...,
        MfaConfiguration: str = ...,
        Policies: "UserPool.Policies" = ...,
        Schema: List["UserPool.SchemaAttribute"] = ...,
        SmsAuthenticationMessage: str = ...,
        SmsConfiguration: "UserPool.SmsConfiguration" = ...,
        SmsVerificationMessage: str = ...,
        UpdateReplacePolicy: str = ...,
        UserPoolAddOns: "UserPool.UserPoolAddOns" = ...,
        UserPoolName: str = ...,
        UserPoolTags: Any = ...,
        UsernameAttributes: List[str] = ...,
        UsernameConfiguration: "UserPool.UsernameConfiguration" = ...,
        VerificationMessageTemplate: "UserPool.VerificationMessageTemplate" = ...
    ): ...
    class AccountRecoverySetting:
        def __init__(
            self, *, RecoveryMechanisms: List["UserPool.RecoveryOption"] = ...
        ): ...
    class AdminCreateUserConfig:
        def __init__(
            self,
            *,
            AllowAdminCreateUserOnly: bool = ...,
            InviteMessageTemplate: "UserPool.InviteMessageTemplate" = ...,
            UnusedAccountValidityDays: int = ...
        ): ...
    class DeviceConfiguration:
        def __init__(
            self,
            *,
            ChallengeRequiredOnNewDevice: bool = ...,
            DeviceOnlyRememberedOnUserPrompt: bool = ...
        ): ...
    class EmailConfiguration:
        def __init__(
            self,
            *,
            ConfigurationSet: str = ...,
            EmailSendingAccount: str = ...,
            From: str = ...,
            ReplyToEmailAddress: str = ...,
            SourceArn: str = ...
        ): ...
    class InviteMessageTemplate:
        def __init__(
            self,
            *,
            EmailMessage: str = ...,
            EmailSubject: str = ...,
            SMSMessage: str = ...
        ): ...
    class LambdaConfig:
        def __init__(
            self,
            *,
            CreateAuthChallenge: str = ...,
            CustomMessage: str = ...,
            DefineAuthChallenge: str = ...,
            PostAuthentication: str = ...,
            PostConfirmation: str = ...,
            PreAuthentication: str = ...,
            PreSignUp: str = ...,
            PreTokenGeneration: str = ...,
            UserMigration: str = ...,
            VerifyAuthChallengeResponse: str = ...
        ): ...
    class NumberAttributeConstraints:
        def __init__(self, *, MaxValue: str = ..., MinValue: str = ...): ...
    class PasswordPolicy:
        def __init__(
            self,
            *,
            MinimumLength: int = ...,
            RequireLowercase: bool = ...,
            RequireNumbers: bool = ...,
            RequireSymbols: bool = ...,
            RequireUppercase: bool = ...,
            TemporaryPasswordValidityDays: int = ...
        ): ...
    class Policies:
        def __init__(self, *, PasswordPolicy: "UserPool.PasswordPolicy" = ...): ...
    class RecoveryOption:
        def __init__(self, *, Name: str = ..., Priority: int = ...): ...
    class SchemaAttribute:
        def __init__(
            self,
            *,
            AttributeDataType: str = ...,
            DeveloperOnlyAttribute: bool = ...,
            Mutable: bool = ...,
            Name: str = ...,
            NumberAttributeConstraints: "UserPool.NumberAttributeConstraints" = ...,
            Required: bool = ...,
            StringAttributeConstraints: "UserPool.StringAttributeConstraints" = ...
        ): ...
    class SmsConfiguration:
        def __init__(self, *, ExternalId: str = ..., SnsCallerArn: str = ...): ...
    class StringAttributeConstraints:
        def __init__(self, *, MaxLength: str = ..., MinLength: str = ...): ...
    class UserPoolAddOns:
        def __init__(self, *, AdvancedSecurityMode: str = ...): ...
    class UsernameConfiguration:
        def __init__(self, *, CaseSensitive: bool = ...): ...
    class VerificationMessageTemplate:
        def __init__(
            self,
            *,
            DefaultEmailOption: str = ...,
            EmailMessage: str = ...,
            EmailMessageByLink: str = ...,
            EmailSubject: str = ...,
            EmailSubjectByLink: str = ...,
            SmsMessage: str = ...
        ): ...

class UserPoolClient:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolclient.html"""

    ClientSecret: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        UserPoolId: str,
        AllowedOAuthFlows: List[str] = ...,
        AllowedOAuthFlowsUserPoolClient: bool = ...,
        AllowedOAuthScopes: List[str] = ...,
        AnalyticsConfiguration: "UserPoolClient.AnalyticsConfiguration" = ...,
        CallbackURLs: List[str] = ...,
        ClientName: str = ...,
        DefaultRedirectURI: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ExplicitAuthFlows: List[str] = ...,
        GenerateSecret: bool = ...,
        LogoutURLs: List[str] = ...,
        PreventUserExistenceErrors: str = ...,
        ReadAttributes: List[str] = ...,
        RefreshTokenValidity: int = ...,
        SupportedIdentityProviders: List[str] = ...,
        UpdateReplacePolicy: str = ...,
        WriteAttributes: List[str] = ...
    ): ...
    class AnalyticsConfiguration:
        def __init__(
            self,
            *,
            ApplicationId: str = ...,
            ExternalId: str = ...,
            RoleArn: str = ...,
            UserDataShared: bool = ...
        ): ...

class UserPoolDomain:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooldomain.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Domain: str,
        UserPoolId: str,
        CustomDomainConfig: "UserPoolDomain.CustomDomainConfigType" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CustomDomainConfigType:
        def __init__(self, *, CertificateArn: str = ...): ...

class UserPoolGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolgroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        UserPoolId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        GroupName: str = ...,
        Precedence: float = ...,
        RoleArn: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class UserPoolIdentityProvider:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolidentityprovider.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ProviderName: str,
        ProviderType: str,
        UserPoolId: str,
        AttributeMapping: Any = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        IdpIdentifiers: List[str] = ...,
        ProviderDetails: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class UserPoolResourceServer:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolresourceserver.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Identifier: str,
        Name: str,
        UserPoolId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Scopes: List["UserPoolResourceServer.ResourceServerScopeType"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ResourceServerScopeType:
        def __init__(self, *, ScopeDescription: str, ScopeName: str): ...

class UserPoolRiskConfigurationAttachment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolriskconfigurationattachment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ClientId: str,
        UserPoolId: str,
        AccountTakeoverRiskConfiguration: "UserPoolRiskConfigurationAttachment.AccountTakeoverRiskConfigurationType" = ...,
        CompromisedCredentialsRiskConfiguration: "UserPoolRiskConfigurationAttachment.CompromisedCredentialsRiskConfigurationType" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RiskExceptionConfiguration: "UserPoolRiskConfigurationAttachment.RiskExceptionConfigurationType" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AccountTakeoverActionType:
        def __init__(self, *, EventAction: str, Notify: bool): ...
    class AccountTakeoverActionsType:
        def __init__(
            self,
            *,
            HighAction: "UserPoolRiskConfigurationAttachment.AccountTakeoverActionType" = ...,
            LowAction: "UserPoolRiskConfigurationAttachment.AccountTakeoverActionType" = ...,
            MediumAction: "UserPoolRiskConfigurationAttachment.AccountTakeoverActionType" = ...
        ): ...
    class AccountTakeoverRiskConfigurationType:
        def __init__(
            self,
            *,
            Actions: "UserPoolRiskConfigurationAttachment.AccountTakeoverActionsType",
            NotifyConfiguration: "UserPoolRiskConfigurationAttachment.NotifyConfigurationType" = ...
        ): ...
    class CompromisedCredentialsActionsType:
        def __init__(self, *, EventAction: str): ...
    class CompromisedCredentialsRiskConfigurationType:
        def __init__(
            self,
            *,
            Actions: "UserPoolRiskConfigurationAttachment.CompromisedCredentialsActionsType",
            EventFilter: List[str] = ...
        ): ...
    class NotifyConfigurationType:
        def __init__(
            self,
            *,
            SourceArn: str,
            BlockEmail: "UserPoolRiskConfigurationAttachment.NotifyEmailType" = ...,
            From: str = ...,
            MfaEmail: "UserPoolRiskConfigurationAttachment.NotifyEmailType" = ...,
            NoActionEmail: "UserPoolRiskConfigurationAttachment.NotifyEmailType" = ...,
            ReplyTo: str = ...
        ): ...
    class NotifyEmailType:
        def __init__(
            self, *, Subject: str, HtmlBody: str = ..., TextBody: str = ...
        ): ...
    class RiskExceptionConfigurationType:
        def __init__(
            self,
            *,
            BlockedIPRangeList: List[str] = ...,
            SkippedIPRangeList: List[str] = ...
        ): ...

class UserPoolUICustomizationAttachment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluicustomizationattachment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ClientId: str,
        UserPoolId: str,
        CSS: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class UserPoolUser:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluser.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        UserPoolId: str,
        ClientMetadata: Any = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DesiredDeliveryMediums: List[str] = ...,
        ForceAliasCreation: bool = ...,
        MessageAction: str = ...,
        UpdateReplacePolicy: str = ...,
        UserAttributes: List["UserPoolUser.AttributeType"] = ...,
        Username: str = ...,
        ValidationData: List["UserPoolUser.AttributeType"] = ...
    ): ...
    class AttributeType:
        def __init__(self, *, Name: str = ..., Value: str = ...): ...

class UserPoolUserToGroupAttachment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpoolusertogroupattachment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        GroupName: str,
        UserPoolId: str,
        Username: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
