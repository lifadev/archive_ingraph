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

_NAMESPACE = "AWS::ResourceGroups"

class Group:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-resourcegroups-group.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        ResourceQuery: "Group.ResourceQuery" = ...,
        Tags: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Query:
        def __init__(
            self,
            *,
            ResourceTypeFilters: List[str] = ...,
            StackIdentifier: str = ...,
            TagFilters: List["Group.TagFilter"] = ...
        ): ...
    class ResourceQuery:
        def __init__(self, *, Query: "Group.Query" = ..., Type: str = ...): ...
    class TagFilter:
        def __init__(self, *, Key: str = ..., Values: List[str] = ...): ...
