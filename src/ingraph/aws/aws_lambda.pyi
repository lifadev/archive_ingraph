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

_NAMESPACE = "AWS::Lambda"

class Alias:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-alias.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        FunctionName: str,
        FunctionVersion: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        ProvisionedConcurrencyConfig: "Alias.ProvisionedConcurrencyConfiguration" = ...,
        RoutingConfig: "Alias.AliasRoutingConfiguration" = ...,
        UpdatePolicy: "Alias.UpdatePolicy" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AliasRoutingConfiguration:
        def __init__(
            self, *, AdditionalVersionWeights: List["Alias.VersionWeight"]
        ): ...
    class ProvisionedConcurrencyConfiguration:
        def __init__(self, *, ProvisionedConcurrentExecutions: int): ...
    class UpdatePolicy:
        def __init__(
            self,
            *,
            ApplicationName: str,
            DeploymentGroupName: str,
            AfterAllowTrafficHook: str = ...,
            BeforeAllowTrafficHook: str = ...
        ): ...
    class VersionWeight:
        def __init__(self, *, FunctionVersion: str, FunctionWeight: float): ...

class EventInvokeConfig:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventinvokeconfig.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        FunctionName: str,
        Qualifier: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DestinationConfig: "EventInvokeConfig.DestinationConfig" = ...,
        MaximumEventAgeInSeconds: int = ...,
        MaximumRetryAttempts: int = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DestinationConfig:
        def __init__(
            self,
            *,
            OnFailure: "EventInvokeConfig.OnFailure" = ...,
            OnSuccess: "EventInvokeConfig.OnSuccess" = ...
        ): ...
    class OnFailure:
        def __init__(self, *, Destination: str): ...
    class OnSuccess:
        def __init__(self, *, Destination: str): ...

class EventSourceMapping:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        EventSourceArn: str,
        FunctionName: str,
        BatchSize: int = ...,
        BisectBatchOnFunctionError: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DestinationConfig: "EventSourceMapping.DestinationConfig" = ...,
        Enabled: bool = ...,
        MaximumBatchingWindowInSeconds: int = ...,
        MaximumRecordAgeInSeconds: int = ...,
        MaximumRetryAttempts: int = ...,
        ParallelizationFactor: int = ...,
        StartingPosition: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DestinationConfig:
        def __init__(self, *, OnFailure: "EventSourceMapping.OnFailure"): ...
    class OnFailure:
        def __init__(self, *, Destination: str): ...

class Function:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-function.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Code: "Function.Code",
        Handler: str,
        Role: str,
        Runtime: str,
        DeadLetterConfig: "Function.DeadLetterConfig" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Environment: "Function.Environment" = ...,
        FunctionName: str = ...,
        KmsKeyArn: str = ...,
        Layers: List[str] = ...,
        MemorySize: int = ...,
        ReservedConcurrentExecutions: int = ...,
        Tags: List["Tag"] = ...,
        Timeout: int = ...,
        TracingConfig: "Function.TracingConfig" = ...,
        UpdateReplacePolicy: str = ...,
        VpcConfig: "Function.VpcConfig" = ...
    ): ...
    class Code:
        def __init__(
            self,
            *,
            S3Bucket: str = ...,
            S3Key: str = ...,
            S3ObjectVersion: str = ...,
            ZipFile: str = ...
        ): ...
    class DeadLetterConfig:
        def __init__(self, *, TargetArn: str = ...): ...
    class Environment:
        def __init__(self, *, Variables: Dict[str, str] = ...): ...
    class TracingConfig:
        def __init__(self, *, Mode: str = ...): ...
    class VpcConfig:
        def __init__(self, *, SecurityGroupIds: List[str], SubnetIds: List[str]): ...

class LayerVersion:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Content: "LayerVersion.Content",
        CompatibleRuntimes: List[str] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        LayerName: str = ...,
        LicenseInfo: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Content:
        def __init__(
            self, *, S3Bucket: str, S3Key: str, S3ObjectVersion: str = ...
        ): ...

class LayerVersionPermission:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversionpermission.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Action: str,
        LayerVersionArn: str,
        Principal: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        OrganizationId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Permission:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Action: str,
        FunctionName: str,
        Principal: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EventSourceToken: str = ...,
        SourceAccount: str = ...,
        SourceArn: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Version:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-version.html"""

    Version_: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        FunctionName: str,
        CodeSha256: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        ProvisionedConcurrencyConfig: "Version.ProvisionedConcurrencyConfiguration" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ProvisionedConcurrencyConfiguration:
        def __init__(self, *, ProvisionedConcurrentExecutions: int): ...
