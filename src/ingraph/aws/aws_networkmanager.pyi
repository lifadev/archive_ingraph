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

_NAMESPACE = "AWS::NetworkManager"

class CustomerGatewayAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-customergatewayassociation.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        CustomerGatewayArn: str,
        DeviceId: str,
        GlobalNetworkId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        LinkId: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Device:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-device.html"""

    DeviceArn: Final[str]

    DeviceId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        GlobalNetworkId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Location: "Device.Location" = ...,
        Model: str = ...,
        SerialNumber: str = ...,
        SiteId: str = ...,
        Tags: List["Tag"] = ...,
        Type: str = ...,
        UpdateReplacePolicy: str = ...,
        Vendor: str = ...
    ): ...
    class Location:
        def __init__(
            self, *, Address: str = ..., Latitude: str = ..., Longitude: str = ...
        ): ...

class GlobalNetwork:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-globalnetwork.html"""

    Arn: Final[str]

    Id: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Link:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-link.html"""

    LinkArn: Final[str]

    LinkId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Bandwidth: "Link.Bandwidth",
        GlobalNetworkId: str,
        SiteId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Provider: str = ...,
        Tags: List["Tag"] = ...,
        Type: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Bandwidth:
        def __init__(self, *, DownloadSpeed: int = ..., UploadSpeed: int = ...): ...

class LinkAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-linkassociation.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeviceId: str,
        GlobalNetworkId: str,
        LinkId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Site:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-site.html"""

    SiteArn: Final[str]

    SiteId: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        GlobalNetworkId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Location: "Site.Location" = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Location:
        def __init__(
            self, *, Address: str = ..., Latitude: str = ..., Longitude: str = ...
        ): ...

class TransitGatewayRegistration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-networkmanager-transitgatewayregistration.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        GlobalNetworkId: str,
        TransitGatewayArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
