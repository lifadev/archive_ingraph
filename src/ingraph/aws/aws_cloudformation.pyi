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

_NAMESPACE = "AWS::CloudFormation"

class CustomResource:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ServiceToken: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...,
        **kwargs: Any
    ): ...

class Macro:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudformation-macro.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        FunctionName: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        LogGroupName: str = ...,
        LogRoleARN: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Stack:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-stack.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        TemplateURL: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        NotificationARNs: List[str] = ...,
        Parameters: Dict[str, str] = ...,
        Tags: List["Tag"] = ...,
        TimeoutInMinutes: int = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class WaitCondition:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitcondition.html"""

    Data: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Count: int = ...,
        CreationPolicy: "WaitCondition.CreationPolicy" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Handle: str = ...,
        Timeout: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class CreationPolicy:
        def __init__(self, *, ResourceSignal: "WaitCondition.ResourceSignal" = ...): ...
    class ResourceSignal:
        def __init__(self, *, Count: int = ..., Timeout: str = ...): ...

class WaitConditionHandle:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-waitconditionhandle.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
