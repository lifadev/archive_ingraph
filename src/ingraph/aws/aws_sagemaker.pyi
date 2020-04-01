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

_NAMESPACE = "AWS::SageMaker"

class CodeRepository:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-coderepository.html"""

    CodeRepositoryName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        GitConfig: "CodeRepository.GitConfig",
        CodeRepositoryName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class GitConfig:
        def __init__(
            self, *, RepositoryUrl: str, Branch: str = ..., SecretArn: str = ...
        ): ...

class Endpoint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpoint.html"""

    EndpointName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        EndpointConfigName: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EndpointName: str = ...,
        ExcludeRetainedVariantProperties: List["Endpoint.VariantProperty"] = ...,
        RetainAllVariantProperties: bool = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class VariantProperty:
        def __init__(self, *, VariantPropertyType: str = ...): ...

class EndpointConfig:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-endpointconfig.html"""

    EndpointConfigName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ProductionVariants: List["EndpointConfig.ProductionVariant"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EndpointConfigName: str = ...,
        KmsKeyId: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ProductionVariant:
        def __init__(
            self,
            *,
            InitialInstanceCount: int,
            InitialVariantWeight: float,
            InstanceType: str,
            ModelName: str,
            VariantName: str,
            AcceleratorType: str = ...
        ): ...

class Model:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-model.html"""

    ModelName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ExecutionRoleArn: str,
        Containers: List["Model.ContainerDefinition"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        ModelName: str = ...,
        PrimaryContainer: "Model.ContainerDefinition" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VpcConfig: "Model.VpcConfig" = ...
    ): ...
    class ContainerDefinition:
        def __init__(
            self,
            *,
            Image: str,
            ContainerHostname: str = ...,
            Environment: Any = ...,
            Mode: str = ...,
            ModelDataUrl: str = ...
        ): ...
    class VpcConfig:
        def __init__(self, *, SecurityGroupIds: List[str], Subnets: List[str]): ...

class NotebookInstance:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstance.html"""

    NotebookInstanceName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        InstanceType: str,
        RoleArn: str,
        AcceleratorTypes: List[str] = ...,
        AdditionalCodeRepositories: List[str] = ...,
        DefaultCodeRepository: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DirectInternetAccess: str = ...,
        KmsKeyId: str = ...,
        LifecycleConfigName: str = ...,
        NotebookInstanceName: str = ...,
        RootAccess: str = ...,
        SecurityGroupIds: List[str] = ...,
        SubnetId: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        VolumeSizeInGB: int = ...
    ): ...

class NotebookInstanceLifecycleConfig:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-notebookinstancelifecycleconfig.html"""

    NotebookInstanceLifecycleConfigName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        NotebookInstanceLifecycleConfigName: str = ...,
        OnCreate: List[
            "NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHook"
        ] = ...,
        OnStart: List[
            "NotebookInstanceLifecycleConfig.NotebookInstanceLifecycleHook"
        ] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class NotebookInstanceLifecycleHook:
        def __init__(self, *, Content: str = ...): ...

class Workteam:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-workteam.html"""

    WorkteamName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        MemberDefinitions: List["Workteam.MemberDefinition"] = ...,
        NotificationConfiguration: "Workteam.NotificationConfiguration" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...,
        WorkteamName: str = ...
    ): ...
    class CognitoMemberDefinition:
        def __init__(
            self, *, CognitoClientId: str, CognitoUserGroup: str, CognitoUserPool: str
        ): ...
    class MemberDefinition:
        def __init__(
            self, *, CognitoMemberDefinition: "Workteam.CognitoMemberDefinition"
        ): ...
    class NotificationConfiguration:
        def __init__(self, *, NotificationTopicArn: str): ...
