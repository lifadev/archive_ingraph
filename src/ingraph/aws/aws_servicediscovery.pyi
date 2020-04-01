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

_NAMESPACE = "AWS::ServiceDiscovery"

class HttpNamespace:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-httpnamespace.html"""

    Id: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Instance:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-instance.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        InstanceAttributes: Any,
        ServiceId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InstanceId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class PrivateDnsNamespace:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-privatednsnamespace.html"""

    Id: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        Vpc: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class PublicDnsNamespace:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-publicdnsnamespace.html"""

    Id: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Service:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicediscovery-service.html"""

    Id: Final[str]

    Arn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        DnsConfig: "Service.DnsConfig" = ...,
        HealthCheckConfig: "Service.HealthCheckConfig" = ...,
        HealthCheckCustomConfig: "Service.HealthCheckCustomConfig" = ...,
        Name: str = ...,
        NamespaceId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DnsConfig:
        def __init__(
            self,
            *,
            DnsRecords: List["Service.DnsRecord"],
            NamespaceId: str = ...,
            RoutingPolicy: str = ...
        ): ...
    class DnsRecord:
        def __init__(self, *, TTL: float, Type: str): ...
    class HealthCheckConfig:
        def __init__(
            self, *, Type: str, FailureThreshold: float = ..., ResourcePath: str = ...
        ): ...
    class HealthCheckCustomConfig:
        def __init__(self, *, FailureThreshold: float = ...): ...
