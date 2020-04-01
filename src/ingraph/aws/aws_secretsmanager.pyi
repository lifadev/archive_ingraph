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

_NAMESPACE = "AWS::SecretsManager"

class ResourcePolicy:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-resourcepolicy.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ResourcePolicy: Any,
        SecretId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class RotationSchedule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-rotationschedule.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        SecretId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RotationLambdaARN: str = ...,
        RotationRules: "RotationSchedule.RotationRules" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class RotationRules:
        def __init__(self, *, AutomaticallyAfterDays: int = ...): ...

class Secret:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secret.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        GenerateSecretString: "Secret.GenerateSecretString" = ...,
        KmsKeyId: str = ...,
        Name: str = ...,
        SecretString: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class GenerateSecretString:
        def __init__(
            self,
            *,
            ExcludeCharacters: str = ...,
            ExcludeLowercase: bool = ...,
            ExcludeNumbers: bool = ...,
            ExcludePunctuation: bool = ...,
            ExcludeUppercase: bool = ...,
            GenerateStringKey: str = ...,
            IncludeSpace: bool = ...,
            PasswordLength: int = ...,
            RequireEachIncludedType: bool = ...,
            SecretStringTemplate: str = ...
        ): ...

class SecretTargetAttachment:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-secretsmanager-secrettargetattachment.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        SecretId: str,
        TargetId: str,
        TargetType: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
