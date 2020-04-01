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

_NAMESPACE = "AWS::Route53"

class HealthCheck:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        HealthCheckConfig: "HealthCheck.HealthCheckConfig",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        HealthCheckTags: List["HealthCheck.HealthCheckTag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AlarmIdentifier:
        def __init__(self, *, Name: str, Region: str): ...
    class HealthCheckConfig:
        def __init__(
            self,
            *,
            Type: str,
            AlarmIdentifier: "HealthCheck.AlarmIdentifier" = ...,
            ChildHealthChecks: List[str] = ...,
            EnableSNI: bool = ...,
            FailureThreshold: int = ...,
            FullyQualifiedDomainName: str = ...,
            HealthThreshold: int = ...,
            IPAddress: str = ...,
            InsufficientDataHealthStatus: str = ...,
            Inverted: bool = ...,
            MeasureLatency: bool = ...,
            Port: int = ...,
            Regions: List[str] = ...,
            RequestInterval: int = ...,
            ResourcePath: str = ...,
            SearchString: str = ...
        ): ...
    class HealthCheckTag:
        def __init__(self, *, Key: str, Value: str): ...

class HostedZone:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html"""

    NameServers: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        HostedZoneConfig: "HostedZone.HostedZoneConfig" = ...,
        HostedZoneTags: List["HostedZone.HostedZoneTag"] = ...,
        QueryLoggingConfig: "HostedZone.QueryLoggingConfig" = ...,
        UpdateReplacePolicy: str = ...,
        VPCs: List["HostedZone.VPC"] = ...
    ): ...
    class HostedZoneConfig:
        def __init__(self, *, Comment: str = ...): ...
    class HostedZoneTag:
        def __init__(self, *, Key: str, Value: str): ...
    class QueryLoggingConfig:
        def __init__(self, *, CloudWatchLogsLogGroupArn: str): ...
    class VPC:
        def __init__(self, *, VPCId: str, VPCRegion: str): ...

class RecordSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        Type: str,
        AliasTarget: "RecordSet.AliasTarget" = ...,
        Comment: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Failover: str = ...,
        GeoLocation: "RecordSet.GeoLocation" = ...,
        HealthCheckId: str = ...,
        HostedZoneId: str = ...,
        HostedZoneName: str = ...,
        MultiValueAnswer: bool = ...,
        Region: str = ...,
        ResourceRecords: List[str] = ...,
        SetIdentifier: str = ...,
        TTL: str = ...,
        UpdateReplacePolicy: str = ...,
        Weight: int = ...
    ): ...
    class AliasTarget:
        def __init__(
            self, *, DNSName: str, HostedZoneId: str, EvaluateTargetHealth: bool = ...
        ): ...
    class GeoLocation:
        def __init__(
            self,
            *,
            ContinentCode: str = ...,
            CountryCode: str = ...,
            SubdivisionCode: str = ...
        ): ...

class RecordSetGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Comment: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        HostedZoneId: str = ...,
        HostedZoneName: str = ...,
        RecordSets: List["RecordSetGroup.RecordSet"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AliasTarget:
        def __init__(
            self, *, DNSName: str, HostedZoneId: str, EvaluateTargetHealth: bool = ...
        ): ...
    class GeoLocation:
        def __init__(
            self,
            *,
            ContinentCode: str = ...,
            CountryCode: str = ...,
            SubdivisionCode: str = ...
        ): ...
    class RecordSet:
        def __init__(
            self,
            *,
            Name: str,
            Type: str,
            AliasTarget: "RecordSetGroup.AliasTarget" = ...,
            Comment: str = ...,
            Failover: str = ...,
            GeoLocation: "RecordSetGroup.GeoLocation" = ...,
            HealthCheckId: str = ...,
            HostedZoneId: str = ...,
            HostedZoneName: str = ...,
            MultiValueAnswer: bool = ...,
            Region: str = ...,
            ResourceRecords: List[str] = ...,
            SetIdentifier: str = ...,
            TTL: str = ...,
            Weight: int = ...
        ): ...
