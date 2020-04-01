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

_NAMESPACE = "AWS::CodeStar"

class GitHubRepository:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestar-githubrepository.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        RepositoryAccessToken: str,
        RepositoryName: str,
        RepositoryOwner: str,
        Code: "GitHubRepository.Code" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EnableIssues: bool = ...,
        IsPrivate: bool = ...,
        RepositoryDescription: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Code:
        def __init__(self, *, S3: "GitHubRepository.S3"): ...
    class S3:
        def __init__(self, *, Bucket: str, Key: str, ObjectVersion: str = ...): ...
