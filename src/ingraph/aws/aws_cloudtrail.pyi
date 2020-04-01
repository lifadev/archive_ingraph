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

_NAMESPACE = "AWS::CloudTrail"

class Trail:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudtrail-trail.html"""

    Arn: Final[str]

    SnsTopicArn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        IsLogging: bool,
        S3BucketName: str,
        CloudWatchLogsLogGroupArn: str = ...,
        CloudWatchLogsRoleArn: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        EnableLogFileValidation: bool = ...,
        EventSelectors: List["Trail.EventSelector"] = ...,
        IncludeGlobalServiceEvents: bool = ...,
        IsMultiRegionTrail: bool = ...,
        KMSKeyId: str = ...,
        S3KeyPrefix: str = ...,
        SnsTopicName: str = ...,
        Tags: List["Tag"] = ...,
        TrailName: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class DataResource:
        def __init__(self, *, Type: str, Values: List[str] = ...): ...
    class EventSelector:
        def __init__(
            self,
            *,
            DataResources: List["Trail.DataResource"] = ...,
            IncludeManagementEvents: bool = ...,
            ReadWriteType: str = ...
        ): ...
