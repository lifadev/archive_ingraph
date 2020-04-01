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

_NAMESPACE = "AWS::Amplify"

class App:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-app.html"""

    AppId: Final[str]

    Arn: Final[str]

    DefaultDomain: Final[str]

    AppName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        AccessToken: str = ...,
        AutoBranchCreationConfig: "App.AutoBranchCreationConfig" = ...,
        BasicAuthConfig: "App.BasicAuthConfig" = ...,
        BuildSpec: str = ...,
        CustomRules: List["App.CustomRule"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        EnvironmentVariables: List["App.EnvironmentVariable"] = ...,
        IAMServiceRole: str = ...,
        OauthToken: str = ...,
        Repository: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AutoBranchCreationConfig:
        def __init__(
            self,
            *,
            AutoBranchCreationPatterns: List[str] = ...,
            BasicAuthConfig: "App.BasicAuthConfig" = ...,
            BuildSpec: str = ...,
            EnableAutoBranchCreation: bool = ...,
            EnableAutoBuild: bool = ...,
            EnablePullRequestPreview: bool = ...,
            EnvironmentVariables: List["App.EnvironmentVariable"] = ...,
            PullRequestEnvironmentName: str = ...,
            Stage: str = ...
        ): ...
    class BasicAuthConfig:
        def __init__(
            self,
            *,
            EnableBasicAuth: bool = ...,
            Password: str = ...,
            Username: str = ...
        ): ...
    class CustomRule:
        def __init__(
            self, *, Source: str, Target: str, Condition: str = ..., Status: str = ...
        ): ...
    class EnvironmentVariable:
        def __init__(self, *, Name: str, Value: str): ...

class Branch:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-branch.html"""

    BranchName: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AppId: str,
        BranchName: str,
        BasicAuthConfig: "Branch.BasicAuthConfig" = ...,
        BuildSpec: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        EnableAutoBuild: bool = ...,
        EnablePullRequestPreview: bool = ...,
        EnvironmentVariables: List["Branch.EnvironmentVariable"] = ...,
        PullRequestEnvironmentName: str = ...,
        Stage: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class BasicAuthConfig:
        def __init__(
            self, *, Password: str, Username: str, EnableBasicAuth: bool = ...
        ): ...
    class EnvironmentVariable:
        def __init__(self, *, Name: str, Value: str): ...

class Domain:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amplify-domain.html"""

    DomainName: Final[str]

    StatusReason: Final[str]

    Arn: Final[str]

    DomainStatus: Final[str]

    CertificateRecord: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AppId: str,
        DomainName: str,
        SubDomainSettings: List["Domain.SubDomainSetting"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class SubDomainSetting:
        def __init__(self, *, BranchName: str, Prefix: str): ...
