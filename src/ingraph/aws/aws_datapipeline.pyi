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

_NAMESPACE = "AWS::DataPipeline"

class Pipeline:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datapipeline-pipeline.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        ParameterObjects: List["Pipeline.ParameterObject"],
        Activate: bool = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        ParameterValues: List["Pipeline.ParameterValue"] = ...,
        PipelineObjects: List["Pipeline.PipelineObject"] = ...,
        PipelineTags: List["Pipeline.PipelineTag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Field:
        def __init__(
            self, *, Key: str, RefValue: str = ..., StringValue: str = ...
        ): ...
    class ParameterAttribute:
        def __init__(self, *, Key: str, StringValue: str): ...
    class ParameterObject:
        def __init__(
            self, *, Attributes: List["Pipeline.ParameterAttribute"], Id: str
        ): ...
    class ParameterValue:
        def __init__(self, *, Id: str, StringValue: str): ...
    class PipelineObject:
        def __init__(self, *, Fields: List["Pipeline.Field"], Id: str, Name: str): ...
    class PipelineTag:
        def __init__(self, *, Key: str, Value: str): ...
