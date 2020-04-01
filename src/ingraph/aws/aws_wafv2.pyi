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

_NAMESPACE = "AWS::WAFv2"

class IPSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-ipset.html"""

    Arn: Final[str]

    Id: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Addresses: List[str],
        IPAddressVersion: str,
        Scope: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Name: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class RegexPatternSet:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-regexpatternset.html"""

    Arn: Final[str]

    Id: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        RegularExpressionList: List[str],
        Scope: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Name: str = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class RuleGroup:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-rulegroup.html"""

    Arn: Final[str]

    Id: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        Capacity: int,
        Scope: str,
        VisibilityConfig: "RuleGroup.VisibilityConfig",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Name: str = ...,
        Rules: List["RuleGroup.Rule"] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AndStatementOne:
        def __init__(self, *, Statements: List["RuleGroup.StatementTwo"]): ...
    class AndStatementTwo:
        def __init__(self, *, Statements: List["RuleGroup.StatementThree"]): ...
    class ByteMatchStatement:
        def __init__(
            self,
            *,
            FieldToMatch: "RuleGroup.FieldToMatch",
            PositionalConstraint: str,
            SearchString: str,
            TextTransformations: List["RuleGroup.TextTransformation"],
            SearchStringBase64: str = ...
        ): ...
    class FieldToMatch:
        def __init__(
            self,
            *,
            AllQueryArguments: Any = ...,
            Body: Any = ...,
            Method: Any = ...,
            QueryString: Any = ...,
            SingleHeader: Any = ...,
            SingleQueryArgument: Any = ...,
            UriPath: Any = ...
        ): ...
    class GeoMatchStatement:
        def __init__(self, *, CountryCodes: List[str] = ...): ...
    class IPSetReferenceStatement:
        def __init__(self, *, Arn: str): ...
    class NotStatementOne:
        def __init__(self, *, Statement: "RuleGroup.StatementTwo"): ...
    class NotStatementTwo:
        def __init__(self, *, Statement: "RuleGroup.StatementThree"): ...
    class OrStatementOne:
        def __init__(self, *, Statements: List["RuleGroup.StatementTwo"]): ...
    class OrStatementTwo:
        def __init__(self, *, Statements: List["RuleGroup.StatementThree"]): ...
    class RateBasedStatementOne:
        def __init__(
            self,
            *,
            AggregateKeyType: str,
            Limit: int,
            ScopeDownStatement: "RuleGroup.StatementTwo" = ...
        ): ...
    class RateBasedStatementTwo:
        def __init__(
            self,
            *,
            AggregateKeyType: str,
            Limit: int,
            ScopeDownStatement: "RuleGroup.StatementThree" = ...
        ): ...
    class RegexPatternSetReferenceStatement:
        def __init__(
            self,
            *,
            Arn: str,
            FieldToMatch: "RuleGroup.FieldToMatch",
            TextTransformations: List["RuleGroup.TextTransformation"]
        ): ...
    class Rule:
        def __init__(
            self,
            *,
            Name: str,
            Priority: int,
            Statement: "RuleGroup.StatementOne",
            VisibilityConfig: "RuleGroup.VisibilityConfig",
            Action: "RuleGroup.RuleAction" = ...
        ): ...
    class RuleAction:
        def __init__(self, *, Allow: Any = ..., Block: Any = ..., Count: Any = ...): ...
    class SizeConstraintStatement:
        def __init__(
            self,
            *,
            ComparisonOperator: str,
            FieldToMatch: "RuleGroup.FieldToMatch",
            Size: int,
            TextTransformations: List["RuleGroup.TextTransformation"]
        ): ...
    class SqliMatchStatement:
        def __init__(
            self,
            *,
            FieldToMatch: "RuleGroup.FieldToMatch",
            TextTransformations: List["RuleGroup.TextTransformation"]
        ): ...
    class StatementOne:
        def __init__(
            self,
            *,
            AndStatement: "RuleGroup.AndStatementOne" = ...,
            ByteMatchStatement: "RuleGroup.ByteMatchStatement" = ...,
            GeoMatchStatement: "RuleGroup.GeoMatchStatement" = ...,
            IPSetReferenceStatement: "RuleGroup.IPSetReferenceStatement" = ...,
            NotStatement: "RuleGroup.NotStatementOne" = ...,
            OrStatement: "RuleGroup.OrStatementOne" = ...,
            RateBasedStatement: "RuleGroup.RateBasedStatementOne" = ...,
            RegexPatternSetReferenceStatement: "RuleGroup.RegexPatternSetReferenceStatement" = ...,
            SizeConstraintStatement: "RuleGroup.SizeConstraintStatement" = ...,
            SqliMatchStatement: "RuleGroup.SqliMatchStatement" = ...,
            XssMatchStatement: "RuleGroup.XssMatchStatement" = ...
        ): ...
    class StatementThree:
        def __init__(
            self,
            *,
            ByteMatchStatement: "RuleGroup.ByteMatchStatement" = ...,
            GeoMatchStatement: "RuleGroup.GeoMatchStatement" = ...,
            IPSetReferenceStatement: "RuleGroup.IPSetReferenceStatement" = ...,
            RegexPatternSetReferenceStatement: "RuleGroup.RegexPatternSetReferenceStatement" = ...,
            SizeConstraintStatement: "RuleGroup.SizeConstraintStatement" = ...,
            SqliMatchStatement: "RuleGroup.SqliMatchStatement" = ...,
            XssMatchStatement: "RuleGroup.XssMatchStatement" = ...
        ): ...
    class StatementTwo:
        def __init__(
            self,
            *,
            AndStatement: "RuleGroup.AndStatementTwo" = ...,
            ByteMatchStatement: "RuleGroup.ByteMatchStatement" = ...,
            GeoMatchStatement: "RuleGroup.GeoMatchStatement" = ...,
            IPSetReferenceStatement: "RuleGroup.IPSetReferenceStatement" = ...,
            NotStatement: "RuleGroup.NotStatementTwo" = ...,
            OrStatement: "RuleGroup.OrStatementTwo" = ...,
            RateBasedStatement: "RuleGroup.RateBasedStatementTwo" = ...,
            RegexPatternSetReferenceStatement: "RuleGroup.RegexPatternSetReferenceStatement" = ...,
            SizeConstraintStatement: "RuleGroup.SizeConstraintStatement" = ...,
            SqliMatchStatement: "RuleGroup.SqliMatchStatement" = ...,
            XssMatchStatement: "RuleGroup.XssMatchStatement" = ...
        ): ...
    class TextTransformation:
        def __init__(self, *, Priority: int, Type: str): ...
    class VisibilityConfig:
        def __init__(
            self,
            *,
            CloudWatchMetricsEnabled: bool,
            MetricName: str,
            SampledRequestsEnabled: bool
        ): ...
    class XssMatchStatement:
        def __init__(
            self,
            *,
            FieldToMatch: "RuleGroup.FieldToMatch",
            TextTransformations: List["RuleGroup.TextTransformation"]
        ): ...

class WebACL:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webacl.html"""

    Arn: Final[str]

    Capacity: Final[int]

    Id: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        DefaultAction: "WebACL.DefaultAction",
        Scope: str,
        VisibilityConfig: "WebACL.VisibilityConfig",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Description: str = ...,
        Name: str = ...,
        Rules: List["WebACL.Rule"] = ...,
        Tags: List["Tag"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class AndStatementOne:
        def __init__(self, *, Statements: List["WebACL.StatementTwo"]): ...
    class AndStatementTwo:
        def __init__(self, *, Statements: List["WebACL.StatementThree"]): ...
    class ByteMatchStatement:
        def __init__(
            self,
            *,
            FieldToMatch: "WebACL.FieldToMatch",
            PositionalConstraint: str,
            SearchString: str,
            TextTransformations: List["WebACL.TextTransformation"],
            SearchStringBase64: str = ...
        ): ...
    class DefaultAction:
        def __init__(self, *, Allow: Any = ..., Block: Any = ...): ...
    class ExcludedRule:
        def __init__(self, *, Name: str): ...
    class FieldToMatch:
        def __init__(
            self,
            *,
            AllQueryArguments: Any = ...,
            Body: Any = ...,
            Method: Any = ...,
            QueryString: Any = ...,
            SingleHeader: Any = ...,
            SingleQueryArgument: Any = ...,
            UriPath: Any = ...
        ): ...
    class GeoMatchStatement:
        def __init__(self, *, CountryCodes: List[str] = ...): ...
    class IPSetReferenceStatement:
        def __init__(self, *, Arn: str): ...
    class ManagedRuleGroupStatement:
        def __init__(
            self,
            *,
            Name: str,
            VendorName: str,
            ExcludedRules: List["WebACL.ExcludedRule"] = ...
        ): ...
    class NotStatementOne:
        def __init__(self, *, Statement: "WebACL.StatementTwo"): ...
    class NotStatementTwo:
        def __init__(self, *, Statement: "WebACL.StatementThree"): ...
    class OrStatementOne:
        def __init__(self, *, Statements: List["WebACL.StatementTwo"]): ...
    class OrStatementTwo:
        def __init__(self, *, Statements: List["WebACL.StatementThree"]): ...
    class OverrideAction:
        def __init__(self, *, Count: Any = ..., None_: Any = ...): ...
    class RateBasedStatementOne:
        def __init__(
            self,
            *,
            AggregateKeyType: str,
            Limit: int,
            ScopeDownStatement: "WebACL.StatementTwo" = ...
        ): ...
    class RateBasedStatementTwo:
        def __init__(
            self,
            *,
            AggregateKeyType: str,
            Limit: int,
            ScopeDownStatement: "WebACL.StatementThree" = ...
        ): ...
    class RegexPatternSetReferenceStatement:
        def __init__(
            self,
            *,
            Arn: str,
            FieldToMatch: "WebACL.FieldToMatch",
            TextTransformations: List["WebACL.TextTransformation"]
        ): ...
    class Rule:
        def __init__(
            self,
            *,
            Name: str,
            Priority: int,
            Statement: "WebACL.StatementOne",
            VisibilityConfig: "WebACL.VisibilityConfig",
            Action: "WebACL.RuleAction" = ...,
            OverrideAction: "WebACL.OverrideAction" = ...
        ): ...
    class RuleAction:
        def __init__(self, *, Allow: Any = ..., Block: Any = ..., Count: Any = ...): ...
    class RuleGroupReferenceStatement:
        def __init__(
            self, *, Arn: str, ExcludedRules: List["WebACL.ExcludedRule"] = ...
        ): ...
    class SizeConstraintStatement:
        def __init__(
            self,
            *,
            ComparisonOperator: str,
            FieldToMatch: "WebACL.FieldToMatch",
            Size: int,
            TextTransformations: List["WebACL.TextTransformation"]
        ): ...
    class SqliMatchStatement:
        def __init__(
            self,
            *,
            FieldToMatch: "WebACL.FieldToMatch",
            TextTransformations: List["WebACL.TextTransformation"]
        ): ...
    class StatementOne:
        def __init__(
            self,
            *,
            AndStatement: "WebACL.AndStatementOne" = ...,
            ByteMatchStatement: "WebACL.ByteMatchStatement" = ...,
            GeoMatchStatement: "WebACL.GeoMatchStatement" = ...,
            IPSetReferenceStatement: "WebACL.IPSetReferenceStatement" = ...,
            ManagedRuleGroupStatement: "WebACL.ManagedRuleGroupStatement" = ...,
            NotStatement: "WebACL.NotStatementOne" = ...,
            OrStatement: "WebACL.OrStatementOne" = ...,
            RateBasedStatement: "WebACL.RateBasedStatementOne" = ...,
            RegexPatternSetReferenceStatement: "WebACL.RegexPatternSetReferenceStatement" = ...,
            RuleGroupReferenceStatement: "WebACL.RuleGroupReferenceStatement" = ...,
            SizeConstraintStatement: "WebACL.SizeConstraintStatement" = ...,
            SqliMatchStatement: "WebACL.SqliMatchStatement" = ...,
            XssMatchStatement: "WebACL.XssMatchStatement" = ...
        ): ...
    class StatementThree:
        def __init__(
            self,
            *,
            ByteMatchStatement: "WebACL.ByteMatchStatement" = ...,
            GeoMatchStatement: "WebACL.GeoMatchStatement" = ...,
            IPSetReferenceStatement: "WebACL.IPSetReferenceStatement" = ...,
            ManagedRuleGroupStatement: "WebACL.ManagedRuleGroupStatement" = ...,
            RegexPatternSetReferenceStatement: "WebACL.RegexPatternSetReferenceStatement" = ...,
            RuleGroupReferenceStatement: "WebACL.RuleGroupReferenceStatement" = ...,
            SizeConstraintStatement: "WebACL.SizeConstraintStatement" = ...,
            SqliMatchStatement: "WebACL.SqliMatchStatement" = ...,
            XssMatchStatement: "WebACL.XssMatchStatement" = ...
        ): ...
    class StatementTwo:
        def __init__(
            self,
            *,
            AndStatement: "WebACL.AndStatementTwo" = ...,
            ByteMatchStatement: "WebACL.ByteMatchStatement" = ...,
            GeoMatchStatement: "WebACL.GeoMatchStatement" = ...,
            IPSetReferenceStatement: "WebACL.IPSetReferenceStatement" = ...,
            ManagedRuleGroupStatement: "WebACL.ManagedRuleGroupStatement" = ...,
            NotStatement: "WebACL.NotStatementTwo" = ...,
            OrStatement: "WebACL.OrStatementTwo" = ...,
            RateBasedStatement: "WebACL.RateBasedStatementTwo" = ...,
            RegexPatternSetReferenceStatement: "WebACL.RegexPatternSetReferenceStatement" = ...,
            RuleGroupReferenceStatement: "WebACL.RuleGroupReferenceStatement" = ...,
            SizeConstraintStatement: "WebACL.SizeConstraintStatement" = ...,
            SqliMatchStatement: "WebACL.SqliMatchStatement" = ...,
            XssMatchStatement: "WebACL.XssMatchStatement" = ...
        ): ...
    class TextTransformation:
        def __init__(self, *, Priority: int, Type: str): ...
    class VisibilityConfig:
        def __init__(
            self,
            *,
            CloudWatchMetricsEnabled: bool,
            MetricName: str,
            SampledRequestsEnabled: bool
        ): ...
    class XssMatchStatement:
        def __init__(
            self,
            *,
            FieldToMatch: "WebACL.FieldToMatch",
            TextTransformations: List["WebACL.TextTransformation"]
        ): ...

class WebACLAssociation:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wafv2-webaclassociation.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        ResourceArn: str,
        WebACLArn: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
