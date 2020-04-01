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

_NAMESPACE = "AWS::Elasticsearch"

class Domain:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticsearch-domain.html"""

    Arn: Final[str]

    DomainArn: Final[str]

    DomainEndpoint: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AccessPolicies: Any = ...,
        AdvancedOptions: Dict[str, str] = ...,
        CognitoOptions: "Domain.CognitoOptions" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DomainName: str = ...,
        EBSOptions: "Domain.EBSOptions" = ...,
        ElasticsearchClusterConfig: "Domain.ElasticsearchClusterConfig" = ...,
        ElasticsearchVersion: str = ...,
        EncryptionAtRestOptions: "Domain.EncryptionAtRestOptions" = ...,
        LogPublishingOptions: Dict[str, "Domain.LogPublishingOption"] = ...,
        NodeToNodeEncryptionOptions: "Domain.NodeToNodeEncryptionOptions" = ...,
        SnapshotOptions: "Domain.SnapshotOptions" = ...,
        Tags: List["Tag"] = ...,
        UpdatePolicy: "Domain.UpdatePolicy" = ...,
        UpdateReplacePolicy: str = ...,
        VPCOptions: "Domain.VPCOptions" = ...
    ): ...
    class CognitoOptions:
        def __init__(
            self,
            *,
            Enabled: bool = ...,
            IdentityPoolId: str = ...,
            RoleArn: str = ...,
            UserPoolId: str = ...
        ): ...
    class EBSOptions:
        def __init__(
            self,
            *,
            EBSEnabled: bool = ...,
            Iops: int = ...,
            VolumeSize: int = ...,
            VolumeType: str = ...
        ): ...
    class ElasticsearchClusterConfig:
        def __init__(
            self,
            *,
            DedicatedMasterCount: int = ...,
            DedicatedMasterEnabled: bool = ...,
            DedicatedMasterType: str = ...,
            InstanceCount: int = ...,
            InstanceType: str = ...,
            ZoneAwarenessConfig: "Domain.ZoneAwarenessConfig" = ...,
            ZoneAwarenessEnabled: bool = ...
        ): ...
    class EncryptionAtRestOptions:
        def __init__(self, *, Enabled: bool = ..., KmsKeyId: str = ...): ...
    class LogPublishingOption:
        def __init__(
            self, *, CloudWatchLogsLogGroupArn: str = ..., Enabled: bool = ...
        ): ...
    class NodeToNodeEncryptionOptions:
        def __init__(self, *, Enabled: bool = ...): ...
    class SnapshotOptions:
        def __init__(self, *, AutomatedSnapshotStartHour: int = ...): ...
    class UpdatePolicy:
        def __init__(self, *, EnableVersionUpgrade: bool = ...): ...
    class VPCOptions:
        def __init__(
            self, *, SecurityGroupIds: List[str] = ..., SubnetIds: List[str] = ...
        ): ...
    class ZoneAwarenessConfig:
        def __init__(self, *, AvailabilityZoneCount: int = ...): ...
