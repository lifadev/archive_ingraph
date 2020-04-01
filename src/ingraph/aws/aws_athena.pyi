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

_NAMESPACE = "AWS::Athena"

class NamedQuery:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-namedquery.html"""

    Ref: Final[str]

    NamedQueryId: Final[str]
    def __init__(
        self,
        *,
        Database: str,
        QueryString: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Name: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class WorkGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-athena-workgroup.html"""

    CreationTime: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        RecursiveDeleteOption: bool = ...,
        State: str = ...,
        Tags: "WorkGroup.Tags" = ...,
        UpdateReplacePolicy: str = ...,
        WorkGroupConfiguration: "WorkGroup.WorkGroupConfiguration" = ...,
        WorkGroupConfigurationUpdates: "WorkGroup.WorkGroupConfigurationUpdates" = ...
    ): ...
    class EncryptionConfiguration:
        def __init__(self, *, EncryptionOption: str, KmsKey: str = ...): ...
    class ResultConfiguration:
        def __init__(
            self,
            *,
            EncryptionConfiguration: "WorkGroup.EncryptionConfiguration" = ...,
            OutputLocation: str = ...
        ): ...
    class ResultConfigurationUpdates:
        def __init__(
            self,
            *,
            EncryptionConfiguration: "WorkGroup.EncryptionConfiguration" = ...,
            OutputLocation: str = ...,
            RemoveEncryptionConfiguration: bool = ...,
            RemoveOutputLocation: bool = ...
        ): ...
    class Tags:
        def __init__(self, *, Tags: List["Tag"] = ...): ...
    class WorkGroupConfiguration:
        def __init__(
            self,
            *,
            BytesScannedCutoffPerQuery: int = ...,
            EnforceWorkGroupConfiguration: bool = ...,
            PublishCloudWatchMetricsEnabled: bool = ...,
            RequesterPaysEnabled: bool = ...,
            ResultConfiguration: "WorkGroup.ResultConfiguration" = ...
        ): ...
    class WorkGroupConfigurationUpdates:
        def __init__(
            self,
            *,
            BytesScannedCutoffPerQuery: int = ...,
            EnforceWorkGroupConfiguration: bool = ...,
            PublishCloudWatchMetricsEnabled: bool = ...,
            RemoveBytesScannedCutoffPerQuery: bool = ...,
            RequesterPaysEnabled: bool = ...,
            ResultConfigurationUpdates: "WorkGroup.ResultConfigurationUpdates" = ...
        ): ...
