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

from types import ModuleType
from typing import Final, List, Optional

ACCOUNT_ID: str
"""The AWS account ID of the account of the current stack."""

AVAILABILITY_ZONES: List[str]
"""The list of Availability Zones for the region of the current
stack."""

NOTIFICATION_ARNS: List[str]
"""The list of notification Amazon Resource Names (ARNs) for the current
stack."""

PARTITION: str
"""For standard AWS regions, the partition is `aws`. For other regions,
the partition is `aws-partitionname`. For example, the partition in the
China (Beijing and Ningxia) region is `aws-cn` and the partition in the
AWS GovCloud (US-West) region is `aws-us-gov`."""

REGION: str
"""The AWS Region of the current stack."""

STACK_ID: str
"""The ID of the current stack."""

STACK_NAME: str
"""The name of the current stack."""

URL_SUFFIX: str
"""The suffix for a domain. The suffix is typically `amazonaws.com`, but
might differ by region. For example, the suffix for the China (Beijing)
region is `amazonaws.com.cn`."""

def b64encode(target: str) -> str:
    """Returns the Base64 representation of the input string."""

def cidr(*, block: str, count: int, bits: int) -> List[str]:
    """Returns an array of CIDR address blocks."""

class Asset:
    """Artifact within a package."""

    url: Final[str]
    uri: Final[str]
    bucket: Final[str]
    key: Final[str]
    text: Final[str]
    def __init__(
        self,
        *,
        name: str,
        package: Optional[ModuleType] = ...,
        compress: Optional[bool] = ...,
    ): ...

class Tag:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html"""

    def __init__(self, *, Key: str, Value: str) -> None: ...
