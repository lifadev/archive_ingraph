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

_NAMESPACE = "AWS::ServiceCatalog"

class AcceptedPortfolioShare:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-acceptedportfolioshare.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PortfolioId: str,
        AcceptLanguage: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class CloudFormationProduct:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationproduct.html"""

    ProductName: Final[str]

    ProvisioningArtifactIds: Final[str]

    ProvisioningArtifactNames: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        Owner: str,
        ProvisioningArtifactParameters: List[
            "CloudFormationProduct.ProvisioningArtifactProperties"
        ],
        AcceptLanguage: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Distributor: str = ...,
        SupportDescription: str = ...,
        SupportEmail: str = ...,
        SupportUrl: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ProvisioningArtifactProperties:
        def __init__(
            self,
            *,
            Info: Any,
            Description: str = ...,
            DisableTemplateValidation: bool = ...,
            Name: str = ...
        ): ...

class CloudFormationProvisionedProduct:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html"""

    CloudformationStackArn: Final[str]

    RecordId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AcceptLanguage: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        NotificationArns: List[str] = ...,
        PathId: str = ...,
        ProductId: str = ...,
        ProductName: str = ...,
        ProvisionedProductName: str = ...,
        ProvisioningArtifactId: str = ...,
        ProvisioningArtifactName: str = ...,
        ProvisioningParameters: List[
            "CloudFormationProvisionedProduct.ProvisioningParameter"
        ] = ...,
        ProvisioningPreferences: "CloudFormationProvisionedProduct.ProvisioningPreferences" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ProvisioningParameter:
        def __init__(self, *, Key: str = ..., Value: str = ...): ...
    class ProvisioningPreferences:
        def __init__(
            self,
            *,
            StackSetAccounts: List[str] = ...,
            StackSetFailureToleranceCount: int = ...,
            StackSetFailureTolerancePercentage: int = ...,
            StackSetMaxConcurrencyCount: int = ...,
            StackSetMaxConcurrencyPercentage: int = ...,
            StackSetOperationType: str = ...,
            StackSetRegions: List[str] = ...
        ): ...

class LaunchNotificationConstraint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchnotificationconstraint.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        NotificationArns: List[str],
        PortfolioId: str,
        ProductId: str,
        AcceptLanguage: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class LaunchRoleConstraint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchroleconstraint.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PortfolioId: str,
        ProductId: str,
        AcceptLanguage: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        LocalRoleName: str = ...,
        RoleArn: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class LaunchTemplateConstraint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-launchtemplateconstraint.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PortfolioId: str,
        ProductId: str,
        Rules: str,
        AcceptLanguage: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Portfolio:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolio.html"""

    PortfolioName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DisplayName: str,
        ProviderName: str,
        AcceptLanguage: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class PortfolioPrincipalAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioprincipalassociation.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PortfolioId: str,
        PrincipalARN: str,
        PrincipalType: str,
        AcceptLanguage: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class PortfolioProductAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioproductassociation.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PortfolioId: str,
        ProductId: str,
        AcceptLanguage: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        SourcePortfolioId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class PortfolioShare:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-portfolioshare.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AccountId: str,
        PortfolioId: str,
        AcceptLanguage: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class ResourceUpdateConstraint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-resourceupdateconstraint.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        PortfolioId: str,
        ProductId: str,
        TagUpdateOnProvisionedProduct: str,
        AcceptLanguage: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class StackSetConstraint:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-stacksetconstraint.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AccountList: List[str],
        AdminRole: str,
        Description: str,
        ExecutionRole: str,
        PortfolioId: str,
        ProductId: str,
        RegionList: List[str],
        StackInstanceControl: str,
        AcceptLanguage: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class TagOption:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoption.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Key: str,
        Value: str,
        Active: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class TagOptionAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-tagoptionassociation.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ResourceId: str,
        TagOptionId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
