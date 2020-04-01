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

_NAMESPACE = "AWS::OpsWorksCM"

class Server:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-opsworkscm-server.html"""

    Endpoint: Final[str]

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        InstanceProfileArn: str,
        InstanceType: str,
        ServiceRoleArn: str,
        AssociatePublicIpAddress: bool = ...,
        BackupId: str = ...,
        BackupRetentionCount: int = ...,
        CustomCertificate: str = ...,
        CustomDomain: str = ...,
        CustomPrivateKey: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        DisableAutomatedBackup: bool = ...,
        Engine: str = ...,
        EngineAttributes: List["Server.EngineAttribute"] = ...,
        EngineModel: str = ...,
        EngineVersion: str = ...,
        KeyPair: str = ...,
        PreferredBackupWindow: str = ...,
        PreferredMaintenanceWindow: str = ...,
        SecurityGroupIds: List[str] = ...,
        ServerName: str = ...,
        SubnetIds: List[str] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class EngineAttribute:
        def __init__(self, *, Name: str = ..., Value: str = ...): ...
