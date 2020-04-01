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

_NAMESPACE = "AWS::AmazonMQ"

class Broker:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-broker.html"""

    IpAddresses: Final[List[str]]

    OpenWireEndpoints: Final[List[str]]

    ConfigurationRevision: Final[int]

    StompEndpoints: Final[List[str]]

    MqttEndpoints: Final[List[str]]

    AmqpEndpoints: Final[List[str]]

    Arn: Final[str]

    ConfigurationId: Final[str]

    WssEndpoints: Final[List[str]]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AutoMinorVersionUpgrade: bool,
        BrokerName: str,
        DeploymentMode: str,
        EngineType: str,
        EngineVersion: str,
        HostInstanceType: str,
        PubliclyAccessible: bool,
        Users: List["Broker.User"],
        Configuration: "Broker.ConfigurationId_" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EncryptionOptions: "Broker.EncryptionOptions" = ...,
        Logs: "Broker.LogList" = ...,
        MaintenanceWindowStartTime: "Broker.MaintenanceWindow" = ...,
        SecurityGroups: List[str] = ...,
        StorageType: str = ...,
        SubnetIds: List[str] = ...,
        Tags: List["Broker.TagsEntry"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ConfigurationId_:
        def __init__(self, *, Id: str, Revision: int): ...
    class EncryptionOptions:
        def __init__(self, *, UseAwsOwnedKey: bool, KmsKeyId: str = ...): ...
    class LogList:
        def __init__(self, *, Audit: bool = ..., General: bool = ...): ...
    class MaintenanceWindow:
        def __init__(self, *, DayOfWeek: str, TimeOfDay: str, TimeZone: str): ...
    class TagsEntry:
        def __init__(self, *, Key: str, Value: str): ...
    class User:
        def __init__(
            self,
            *,
            Password: str,
            Username: str,
            ConsoleAccess: bool = ...,
            Groups: List[str] = ...
        ): ...

class Configuration:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configuration.html"""

    Revision: Final[int]

    Id: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Data: str,
        EngineType: str,
        EngineVersion: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Tags: List["Configuration.TagsEntry"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class TagsEntry:
        def __init__(self, *, Key: str, Value: str): ...

class ConfigurationAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-amazonmq-configurationassociation.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Broker: str,
        Configuration: "ConfigurationAssociation.ConfigurationId",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ConfigurationId:
        def __init__(self, *, Id: str, Revision: int): ...
