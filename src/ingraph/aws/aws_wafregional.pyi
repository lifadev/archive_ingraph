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

_NAMESPACE = "AWS::WAFRegional"

class ByteMatchSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-bytematchset.html"""

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

class GeoMatchSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-geomatchset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        GeoMatchConstraints: List["GeoMatchSet.GeoMatchConstraint"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class GeoMatchConstraint:
        def __init__(self, *, Type: str, Value: str): ...

class IPSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ipset.html"""

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

class RateBasedRule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-ratebasedrule.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        MetricName: str,
        Name: str,
        RateKey: str,
        RateLimit: int,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        MatchPredicates: List["RateBasedRule.Predicate"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Predicate:
        def __init__(self, *, DataId: str, Negated: bool, Type: str): ...

class RegexPatternSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-regexpatternset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        RegexPatternStrings: List[str],
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Rule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-rule.html"""

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
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sizeconstraintset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        SizeConstraints: List["SizeConstraintSet.SizeConstraint"] = ...,
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
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-sqlinjectionmatchset.html"""

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
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webacl.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DefaultAction: "WebACL.Action",
        MetricName: str,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Rules: List["WebACL.Rule"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Action:
        def __init__(self, *, Type: str): ...
    class Rule:
        def __init__(self, *, Action: "WebACL.Action", Priority: int, RuleId: str): ...

class WebACLAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-webaclassociation.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ResourceArn: str,
        WebACLId: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class XssMatchSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafregional-xssmatchset.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Name: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...,
        XssMatchTuples: List["XssMatchSet.XssMatchTuple"] = ...
    ): ...
    class FieldToMatch:
        def __init__(self, *, Type: str, Data: str = ...): ...
    class XssMatchTuple:
        def __init__(
            self, *, FieldToMatch: "XssMatchSet.FieldToMatch", TextTransformation: str
        ): ...
