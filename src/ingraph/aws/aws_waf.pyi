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

_NAMESPACE = "AWS::WAF"

class ByteMatchSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-bytematchset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        ByteMatchTuples: List["ByteMatchSet.ByteMatchTuple"] = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ByteMatchTuple:
        def __init__(
            self,
            *,
            FieldToMatch: "ByteMatchSet.FieldToMatch",
            PositionalConstraint: str,
            TextTransformation: str,
            TargetString: str = ...,
            TargetStringBase64: str = ...
        ): ...
    class FieldToMatch:
        def __init__(self, *, Type: str, Data: str = ...): ...

class IPSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-ipset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        IPSetDescriptors: List["IPSet.IPSetDescriptor"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class IPSetDescriptor:
        def __init__(self, *, Type: str, Value: str): ...

class Rule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-rule.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        MetricName: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Predicates: List["Rule.Predicate"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Predicate:
        def __init__(self, *, DataId: str, Negated: bool, Type: str): ...

class SizeConstraintSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sizeconstraintset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        SizeConstraints: List["SizeConstraintSet.SizeConstraint"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class FieldToMatch:
        def __init__(self, *, Type: str, Data: str = ...): ...
    class SizeConstraint:
        def __init__(
            self,
            *,
            ComparisonOperator: str,
            FieldToMatch: "SizeConstraintSet.FieldToMatch",
            Size: int,
            TextTransformation: str
        ): ...

class SqlInjectionMatchSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-sqlinjectionmatchset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        SqlInjectionMatchTuples: List[
            "SqlInjectionMatchSet.SqlInjectionMatchTuple"
        ] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class FieldToMatch:
        def __init__(self, *, Type: str, Data: str = ...): ...
    class SqlInjectionMatchTuple:
        def __init__(
            self,
            *,
            FieldToMatch: "SqlInjectionMatchSet.FieldToMatch",
            TextTransformation: str
        ): ...

class WebACL:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-webacl.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DefaultAction: "WebACL.WafAction",
        MetricName: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Rules: List["WebACL.ActivatedRule"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class ActivatedRule:
        def __init__(
            self, *, Priority: int, RuleId: str, Action: "WebACL.WafAction" = ...
        ): ...
    class WafAction:
        def __init__(self, *, Type: str): ...

class XssMatchSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-waf-xssmatchset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        XssMatchTuples: List["XssMatchSet.XssMatchTuple"],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class FieldToMatch:
        def __init__(self, *, Type: str, Data: str = ...): ...
    class XssMatchTuple:
        def __init__(
            self, *, FieldToMatch: "XssMatchSet.FieldToMatch", TextTransformation: str
        ): ...
