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

_NAMESPACE = "AWS::DynamoDB"

class Table:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.html"""

    Arn: Final[str]

    StreamArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        KeySchema: List["Table.KeySchema"],
        AttributeDefinitions: List["Table.AttributeDefinition"] = ...,
        BillingMode: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        GlobalSecondaryIndexes: List["Table.GlobalSecondaryIndex"] = ...,
        LocalSecondaryIndexes: List["Table.LocalSecondaryIndex"] = ...,
        PointInTimeRecoverySpecification: "Table.PointInTimeRecoverySpecification" = ...,
        ProvisionedThroughput: "Table.ProvisionedThroughput" = ...,
        SSESpecification: "Table.SSESpecification" = ...,
        StreamSpecification: "Table.StreamSpecification" = ...,
        TableName: str = ...,
        Tags: List["Tag"] = ...,
        TimeToLiveSpecification: "Table.TimeToLiveSpecification" = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AttributeDefinition:
        def __init__(self, *, AttributeName: str, AttributeType: str): ...
    class GlobalSecondaryIndex:
        def __init__(
            self,
            *,
            IndexName: str,
            KeySchema: List["Table.KeySchema"],
            Projection: "Table.Projection",
            ProvisionedThroughput: "Table.ProvisionedThroughput" = ...
        ): ...
    class KeySchema:
        def __init__(self, *, AttributeName: str, KeyType: str): ...
    class LocalSecondaryIndex:
        def __init__(
            self,
            *,
            IndexName: str,
            KeySchema: List["Table.KeySchema"],
            Projection: "Table.Projection"
        ): ...
    class PointInTimeRecoverySpecification:
        def __init__(self, *, PointInTimeRecoveryEnabled: bool = ...): ...
    class Projection:
        def __init__(
            self, *, NonKeyAttributes: List[str] = ..., ProjectionType: str = ...
        ): ...
    class ProvisionedThroughput:
        def __init__(self, *, ReadCapacityUnits: int, WriteCapacityUnits: int): ...
    class SSESpecification:
        def __init__(
            self, *, SSEEnabled: bool, KMSMasterKeyId: str = ..., SSEType: str = ...
        ): ...
    class StreamSpecification:
        def __init__(self, *, StreamViewType: str): ...
    class TimeToLiveSpecification:
        def __init__(self, *, AttributeName: str, Enabled: bool): ...
