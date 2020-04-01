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

_NAMESPACE = "AWS::Cassandra"

class Keyspace:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-keyspace.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        KeyspaceName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Table:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        KeyspaceName: str,
        PartitionKeyColumns: List["Table.Column"],
        BillingMode: "Table.BillingMode" = ...,
        ClusteringKeyColumns: List["Table.ClusteringKeyColumn"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        RegularColumns: List["Table.Column"] = ...,
        TableName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class BillingMode:
        def __init__(
            self,
            *,
            Mode: str,
            ProvisionedThroughput: "Table.ProvisionedThroughput" = ...
        ): ...
    class ClusteringKeyColumn:
        def __init__(self, *, Column: "Table.Column", OrderBy: str = ...): ...
    class Column:
        def __init__(self, *, ColumnName: str, ColumnType: str): ...
    class ProvisionedThroughput:
        def __init__(self, *, ReadCapacityUnits: int, WriteCapacityUnits: int): ...
