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

_NAMESPACE = "AWS::CodePipeline"

class CustomActionType:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-customactiontype.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Category: str,
        InputArtifactDetails: "CustomActionType.ArtifactDetails",
        OutputArtifactDetails: "CustomActionType.ArtifactDetails",
        Provider: str,
        Version: str,
        ConfigurationProperties: List["CustomActionType.ConfigurationProperties"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Settings: "CustomActionType.Settings" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ArtifactDetails:
        def __init__(self, *, MaximumCount: int, MinimumCount: int): ...
    class ConfigurationProperties:
        def __init__(
            self,
            *,
            Key: bool,
            Name: str,
            Required: bool,
            Secret: bool,
            Description: str = ...,
            Queryable: bool = ...,
            Type: str = ...
        ): ...
    class Settings:
        def __init__(
            self,
            *,
            EntityUrlTemplate: str = ...,
            ExecutionUrlTemplate: str = ...,
            RevisionUrlTemplate: str = ...,
            ThirdPartyConfigurationUrl: str = ...
        ): ...

class Pipeline:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-pipeline.html"""

    Version: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        RoleArn: str,
        Stages: List["Pipeline.StageDeclaration"],
        ArtifactStore: "Pipeline.ArtifactStore" = ...,
        ArtifactStores: List["Pipeline.ArtifactStoreMap"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DisableInboundStageTransitions: List["Pipeline.StageTransition"] = ...,
        Name: str = ...,
        RestartExecutionOnUpdate: bool = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ActionDeclaration:
        def __init__(
            self,
            *,
            ActionTypeId: "Pipeline.ActionTypeId",
            Name: str,
            Configuration: Any = ...,
            InputArtifacts: List["Pipeline.InputArtifact"] = ...,
            Namespace: str = ...,
            OutputArtifacts: List["Pipeline.OutputArtifact"] = ...,
            Region: str = ...,
            RoleArn: str = ...,
            RunOrder: int = ...
        ): ...
    class ActionTypeId:
        def __init__(
            self, *, Category: str, Owner: str, Provider: str, Version: str
        ): ...
    class ArtifactStore:
        def __init__(
            self,
            *,
            Location: str,
            Type: str,
            EncryptionKey: "Pipeline.EncryptionKey" = ...
        ): ...
    class ArtifactStoreMap:
        def __init__(self, *, ArtifactStore: "Pipeline.ArtifactStore", Region: str): ...
    class BlockerDeclaration:
        def __init__(self, *, Name: str, Type: str): ...
    class EncryptionKey:
        def __init__(self, *, Id: str, Type: str): ...
    class InputArtifact:
        def __init__(self, *, Name: str): ...
    class OutputArtifact:
        def __init__(self, *, Name: str): ...
    class StageDeclaration:
        def __init__(
            self,
            *,
            Actions: List["Pipeline.ActionDeclaration"],
            Name: str,
            Blockers: List["Pipeline.BlockerDeclaration"] = ...
        ): ...
    class StageTransition:
        def __init__(self, *, Reason: str, StageName: str): ...

class Webhook:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codepipeline-webhook.html"""

    Url: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Authentication: str,
        AuthenticationConfiguration: "Webhook.WebhookAuthConfiguration",
        Filters: List["Webhook.WebhookFilterRule"],
        TargetAction: str,
        TargetPipeline: str,
        TargetPipelineVersion: int,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        RegisterWithThirdParty: bool = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class WebhookAuthConfiguration:
        def __init__(self, *, AllowedIPRange: str = ..., SecretToken: str = ...): ...
    class WebhookFilterRule:
        def __init__(self, *, JsonPath: str, MatchEquals: str = ...): ...
