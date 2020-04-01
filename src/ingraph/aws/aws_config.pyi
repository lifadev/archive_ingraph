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

_NAMESPACE = "AWS::Config"

class AggregationAuthorization:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-aggregationauthorization.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AuthorizedAccountId: str,
        AuthorizedAwsRegion: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ConfigRule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configrule.html"""

    Arn: Final[str]

    Compliance_Type: Final[str]

    ConfigRuleId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Source: "ConfigRule.Source",
        ConfigRuleName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        InputParameters: Any = ...,
        MaximumExecutionFrequency: str = ...,
        Scope: "ConfigRule.Scope" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Scope:
        def __init__(
            self,
            *,
            ComplianceResourceId: str = ...,
            ComplianceResourceTypes: List[str] = ...,
            TagKey: str = ...,
            TagValue: str = ...
        ): ...
    class Source:
        def __init__(
            self,
            *,
            Owner: str,
            SourceIdentifier: str,
            SourceDetails: List["ConfigRule.SourceDetail"] = ...
        ): ...
    class SourceDetail:
        def __init__(
            self,
            *,
            EventSource: str,
            MessageType: str,
            MaximumExecutionFrequency: str = ...
        ): ...

class ConfigurationAggregator:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationaggregator.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ConfigurationAggregatorName: str,
        AccountAggregationSources: List[
            "ConfigurationAggregator.AccountAggregationSource"
        ] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        OrganizationAggregationSource: "ConfigurationAggregator.OrganizationAggregationSource" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AccountAggregationSource:
        def __init__(
            self,
            *,
            AccountIds: List[str],
            AllAwsRegions: bool = ...,
            AwsRegions: List[str] = ...
        ): ...
    class OrganizationAggregationSource:
        def __init__(
            self,
            *,
            RoleArn: str,
            AllAwsRegions: bool = ...,
            AwsRegions: List[str] = ...
        ): ...

class ConfigurationRecorder:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-configurationrecorder.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        RoleARN: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        RecordingGroup: "ConfigurationRecorder.RecordingGroup" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class RecordingGroup:
        def __init__(
            self,
            *,
            AllSupported: bool = ...,
            IncludeGlobalResourceTypes: bool = ...,
            ResourceTypes: List[str] = ...
        ): ...

class ConformancePack:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-conformancepack.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ConformancePackName: str,
        DeliveryS3Bucket: str,
        ConformancePackInputParameters: List[
            "ConformancePack.ConformancePackInputParameter"
        ] = ...,
        DeletionPolicy: str = ...,
        DeliveryS3KeyPrefix: str = ...,
        DependsOn: List[Any] = ...,
        TemplateBody: str = ...,
        TemplateS3Uri: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ConformancePackInputParameter:
        def __init__(self, *, ParameterName: str, ParameterValue: str): ...

class DeliveryChannel:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-deliverychannel.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        S3BucketName: str,
        ConfigSnapshotDeliveryProperties: "DeliveryChannel.ConfigSnapshotDeliveryProperties" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        S3KeyPrefix: str = ...,
        SnsTopicARN: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ConfigSnapshotDeliveryProperties:
        def __init__(self, *, DeliveryFrequency: str = ...): ...

class OrganizationConfigRule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconfigrule.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        OrganizationConfigRuleName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ExcludedAccounts: List[str] = ...,
        OrganizationCustomRuleMetadata: "OrganizationConfigRule.OrganizationCustomRuleMetadata" = ...,
        OrganizationManagedRuleMetadata: "OrganizationConfigRule.OrganizationManagedRuleMetadata" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class OrganizationCustomRuleMetadata:
        def __init__(
            self,
            *,
            LambdaFunctionArn: str,
            OrganizationConfigRuleTriggerTypes: List[str],
            Description: str = ...,
            InputParameters: str = ...,
            MaximumExecutionFrequency: str = ...,
            ResourceIdScope: str = ...,
            ResourceTypesScope: List[str] = ...,
            TagKeyScope: str = ...,
            TagValueScope: str = ...
        ): ...
    class OrganizationManagedRuleMetadata:
        def __init__(
            self,
            *,
            RuleIdentifier: str,
            Description: str = ...,
            InputParameters: str = ...,
            MaximumExecutionFrequency: str = ...,
            ResourceIdScope: str = ...,
            ResourceTypesScope: List[str] = ...,
            TagKeyScope: str = ...,
            TagValueScope: str = ...
        ): ...

class OrganizationConformancePack:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-organizationconformancepack.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeliveryS3Bucket: str,
        OrganizationConformancePackName: str,
        ConformancePackInputParameters: List[
            "OrganizationConformancePack.ConformancePackInputParameter"
        ] = ...,
        DeletionPolicy: str = ...,
        DeliveryS3KeyPrefix: str = ...,
        DependsOn: List[Any] = ...,
        ExcludedAccounts: List[str] = ...,
        TemplateBody: str = ...,
        TemplateS3Uri: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ConformancePackInputParameter:
        def __init__(self, *, ParameterName: str, ParameterValue: str): ...

class RemediationConfiguration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-config-remediationconfiguration.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ConfigRuleName: str,
        TargetId: str,
        TargetType: str,
        Automatic: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ExecutionControls: "RemediationConfiguration.ExecutionControls" = ...,
        MaximumAutomaticAttempts: int = ...,
        Parameters: Any = ...,
        ResourceType: str = ...,
        RetryAttemptSeconds: int = ...,
        TargetVersion: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ExecutionControls:
        def __init__(
            self, *, SsmControls: "RemediationConfiguration.SsmControls" = ...
        ): ...
    class RemediationParameterValue:
        def __init__(
            self,
            *,
            ResourceValue: "RemediationConfiguration.ResourceValue" = ...,
            StaticValue: "RemediationConfiguration.StaticValue" = ...
        ): ...
    class ResourceValue:
        def __init__(self, *, Value: str = ...): ...
    class SsmControls:
        def __init__(
            self,
            *,
            ConcurrentExecutionRatePercentage: int = ...,
            ErrorPercentage: int = ...
        ): ...
    class StaticValue:
        def __init__(self, *, Values: List[str] = ...): ...
