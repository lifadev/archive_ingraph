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

_NAMESPACE = "AWS::ACMPCA"

class Certificate:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificate.html"""

    Certificate_: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        CertificateAuthorityArn: str,
        CertificateSigningRequest: str,
        SigningAlgorithm: str,
        Validity: Any,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        TemplateArn: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Validity:
        def __init__(self, *, Type: str, Value: int): ...

class CertificateAuthority:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthority.html"""

    Arn: Final[str]

    CertificateSigningRequest: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        KeyAlgorithm: str,
        SigningAlgorithm: str,
        Subject: Any,
        Type: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RevocationConfiguration: Any = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CrlConfiguration:
        def __init__(
            self,
            *,
            CustomCname: str = ...,
            Enabled: bool = ...,
            ExpirationInDays: int = ...,
            S3BucketName: str = ...
        ): ...
    class RevocationConfiguration:
        def __init__(
            self, *, CrlConfiguration: "CertificateAuthority.CrlConfiguration" = ...
        ): ...
    class Subject:
        def __init__(
            self,
            *,
            CommonName: str = ...,
            Country: str = ...,
            DistinguishedNameQualifier: str = ...,
            GenerationQualifier: str = ...,
            GivenName: str = ...,
            Initials: str = ...,
            Locality: str = ...,
            Organization: str = ...,
            OrganizationalUnit: str = ...,
            Pseudonym: str = ...,
            SerialNumber: str = ...,
            State: str = ...,
            Surname: str = ...,
            Title: str = ...
        ): ...

class CertificateAuthorityActivation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-acmpca-certificateauthorityactivation.html"""

    CompleteCertificateChain: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Certificate: str,
        CertificateAuthorityArn: str,
        CertificateChain: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Status: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
