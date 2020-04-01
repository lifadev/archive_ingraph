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

_NAMESPACE = "Alexa::ASK"

class Skill:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        AuthenticationConfiguration: "Skill.AuthenticationConfiguration",
        SkillPackage: "Skill.SkillPackage",
        VendorId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AuthenticationConfiguration:
        def __init__(self, *, ClientId: str, ClientSecret: str, RefreshToken: str): ...
    class Overrides:
        def __init__(self, *, Manifest: Any = ...): ...
    class SkillPackage:
        def __init__(
            self,
            *,
            S3Bucket: str,
            S3Key: str,
            Overrides: "Skill.Overrides" = ...,
            S3BucketRole: str = ...,
            S3ObjectVersion: str = ...
        ): ...
