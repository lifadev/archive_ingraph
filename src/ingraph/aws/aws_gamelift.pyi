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

_NAMESPACE = "AWS::GameLift"

class Alias:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        RoutingStrategy: "Alias.RoutingStrategy",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class RoutingStrategy:
        def __init__(self, *, Type: str, FleetId: str = ..., Message: str = ...): ...

class Build:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        OperatingSystem: str = ...,
        StorageLocation: "Build.S3Location" = ...,
        UpdateReplacePolicy: str = ...,
        Version: str = ...
    ): ...
    class S3Location:
        def __init__(
            self, *, Bucket: str, Key: str, RoleArn: str, ObjectVersion: str = ...
        ): ...

class Fleet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        EC2InstanceType: str,
        Name: str,
        BuildId: str = ...,
        CertificateConfiguration: "Fleet.CertificateConfiguration" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        DesiredEC2Instances: int = ...,
        EC2InboundPermissions: List["Fleet.IpPermission"] = ...,
        FleetType: str = ...,
        InstanceRoleARN: str = ...,
        LogPaths: List[str] = ...,
        MaxSize: int = ...,
        MetricGroups: List[str] = ...,
        MinSize: int = ...,
        NewGameSessionProtectionPolicy: str = ...,
        PeerVpcAwsAccountId: str = ...,
        PeerVpcId: str = ...,
        ResourceCreationLimitPolicy: "Fleet.ResourceCreationLimitPolicy" = ...,
        RuntimeConfiguration: "Fleet.RuntimeConfiguration" = ...,
        ScriptId: str = ...,
        ServerLaunchParameters: str = ...,
        ServerLaunchPath: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CertificateConfiguration:
        def __init__(self, *, CertificateType: str): ...
    class IpPermission:
        def __init__(
            self, *, FromPort: int, IpRange: str, Protocol: str, ToPort: int
        ): ...
    class ResourceCreationLimitPolicy:
        def __init__(
            self,
            *,
            NewGameSessionsPerCreator: int = ...,
            PolicyPeriodInMinutes: int = ...
        ): ...
    class RuntimeConfiguration:
        def __init__(
            self,
            *,
            GameSessionActivationTimeoutSeconds: int = ...,
            MaxConcurrentGameSessionActivations: int = ...,
            ServerProcesses: List["Fleet.ServerProcess"] = ...
        ): ...
    class ServerProcess:
        def __init__(
            self, *, ConcurrentExecutions: int, LaunchPath: str, Parameters: str = ...
        ): ...

class GameSessionQueue:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html"""

    Arn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Destinations: List["GameSessionQueue.Destination"] = ...,
        PlayerLatencyPolicies: List["GameSessionQueue.PlayerLatencyPolicy"] = ...,
        TimeoutInSeconds: int = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Destination:
        def __init__(self, *, DestinationArn: str = ...): ...
    class PlayerLatencyPolicy:
        def __init__(
            self,
            *,
            MaximumIndividualPlayerLatencyMilliseconds: int = ...,
            PolicyDurationSeconds: int = ...
        ): ...

class MatchmakingConfiguration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html"""

    Arn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AcceptanceRequired: bool,
        GameSessionQueueArns: List[str],
        Name: str,
        RequestTimeoutSeconds: int,
        RuleSetName: str,
        AcceptanceTimeoutSeconds: int = ...,
        AdditionalPlayerCount: int = ...,
        BackfillMode: str = ...,
        CustomEventData: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        GameProperties: List["MatchmakingConfiguration.GameProperty"] = ...,
        GameSessionData: str = ...,
        NotificationTarget: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class GameProperty:
        def __init__(self, *, Key: str, Value: str): ...

class MatchmakingRuleSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html"""

    Arn: Final[str]

    Name: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        RuleSetBody: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Script:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html"""

    Id: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        StorageLocation: "Script.S3Location",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Name: str = ...,
        UpdateReplacePolicy: str = ...,
        Version: str = ...
    ): ...
    class S3Location:
        def __init__(
            self, *, Bucket: str, Key: str, RoleArn: str, ObjectVersion: str = ...
        ): ...
