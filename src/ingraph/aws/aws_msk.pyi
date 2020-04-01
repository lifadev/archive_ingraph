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

_NAMESPACE = "AWS::MSK"

class Cluster:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-msk-cluster.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        BrokerNodeGroupInfo: "Cluster.BrokerNodeGroupInfo",
        ClusterName: str,
        KafkaVersion: str,
        NumberOfBrokerNodes: int,
        ClientAuthentication: "Cluster.ClientAuthentication" = ...,
        ConfigurationInfo: "Cluster.ConfigurationInfo" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EncryptionInfo: "Cluster.EncryptionInfo" = ...,
        EnhancedMonitoring: str = ...,
        LoggingInfo: "Cluster.LoggingInfo" = ...,
        OpenMonitoring: "Cluster.OpenMonitoring" = ...,
        Tags: Any = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class BrokerLogs:
        def __init__(
            self,
            *,
            CloudWatchLogs: "Cluster.CloudWatchLogs" = ...,
            Firehose: "Cluster.Firehose" = ...,
            S3: "Cluster.S3" = ...
        ): ...
    class BrokerNodeGroupInfo:
        def __init__(
            self,
            *,
            ClientSubnets: List[str],
            InstanceType: str,
            BrokerAZDistribution: str = ...,
            SecurityGroups: List[str] = ...,
            StorageInfo: "Cluster.StorageInfo" = ...
        ): ...
    class ClientAuthentication:
        def __init__(self, *, Tls: "Cluster.Tls" = ...): ...
    class CloudWatchLogs:
        def __init__(self, *, Enabled: bool, LogGroup: str = ...): ...
    class ConfigurationInfo:
        def __init__(self, *, Arn: str, Revision: int): ...
    class EBSStorageInfo:
        def __init__(self, *, VolumeSize: int = ...): ...
    class EncryptionAtRest:
        def __init__(self, *, DataVolumeKMSKeyId: str): ...
    class EncryptionInTransit:
        def __init__(self, *, ClientBroker: str = ..., InCluster: bool = ...): ...
    class EncryptionInfo:
        def __init__(
            self,
            *,
            EncryptionAtRest: "Cluster.EncryptionAtRest" = ...,
            EncryptionInTransit: "Cluster.EncryptionInTransit" = ...
        ): ...
    class Firehose:
        def __init__(self, *, Enabled: bool, DeliveryStream: str = ...): ...
    class JmxExporter:
        def __init__(self, *, EnabledInBroker: bool): ...
    class LoggingInfo:
        def __init__(self, *, BrokerLogs: "Cluster.BrokerLogs"): ...
    class NodeExporter:
        def __init__(self, *, EnabledInBroker: bool): ...
    class OpenMonitoring:
        def __init__(self, *, Prometheus: "Cluster.Prometheus"): ...
    class Prometheus:
        def __init__(
            self,
            *,
            JmxExporter: "Cluster.JmxExporter" = ...,
            NodeExporter: "Cluster.NodeExporter" = ...
        ): ...
    class S3:
        def __init__(self, *, Enabled: bool, Bucket: str = ..., Prefix: str = ...): ...
    class StorageInfo:
        def __init__(self, *, EBSStorageInfo: "Cluster.EBSStorageInfo" = ...): ...
    class Tls:
        def __init__(self, *, CertificateAuthorityArnList: List[str] = ...): ...
