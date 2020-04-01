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

_NAMESPACE = "AWS::CloudWatch"

class Alarm:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cw-alarm.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        ComparisonOperator: str,
        EvaluationPeriods: int,
        ActionsEnabled: bool = ...,
        AlarmActions: List[str] = ...,
        AlarmDescription: str = ...,
        AlarmName: str = ...,
        DatapointsToAlarm: int = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Dimensions: List["Alarm.Dimension"] = ...,
        EvaluateLowSampleCountPercentile: str = ...,
        ExtendedStatistic: str = ...,
        InsufficientDataActions: List[str] = ...,
        MetricName: str = ...,
        Metrics: List["Alarm.MetricDataQuery"] = ...,
        Namespace: str = ...,
        OKActions: List[str] = ...,
        Period: int = ...,
        Statistic: str = ...,
        Threshold: float = ...,
        ThresholdMetricId: str = ...,
        TreatMissingData: str = ...,
        Unit: str = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Dimension:
        def __init__(self, *, Name: str, Value: str): ...
    class Metric:
        def __init__(
            self,
            *,
            Dimensions: List["Alarm.Dimension"] = ...,
            MetricName: str = ...,
            Namespace: str = ...
        ): ...
    class MetricDataQuery:
        def __init__(
            self,
            *,
            Id: str,
            Expression: str = ...,
            Label: str = ...,
            MetricStat: "Alarm.MetricStat" = ...,
            ReturnData: bool = ...
        ): ...
    class MetricStat:
        def __init__(
            self, *, Metric: "Alarm.Metric", Period: int, Stat: str, Unit: str = ...
        ): ...

class AnomalyDetector:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        MetricName: str,
        Namespace: str,
        Stat: str,
        Configuration: "AnomalyDetector.Configuration" = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        Dimensions: List["AnomalyDetector.Dimension"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class Configuration:
        def __init__(
            self,
            *,
            ExcludedTimeRanges: List["AnomalyDetector.Range"] = ...,
            MetricTimeZone: str = ...
        ): ...
    class Dimension:
        def __init__(self, *, Name: str, Value: str): ...
    class Range:
        def __init__(self, *, EndTime: str, StartTime: str): ...

class CompositeAlarm:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html"""

    Arn: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        AlarmName: str,
        AlarmRule: str,
        ActionsEnabled: bool = ...,
        AlarmActions: List[str] = ...,
        AlarmDescription: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        InsufficientDataActions: List[str] = ...,
        OKActions: List[str] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class Dashboard:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        DashboardBody: str,
        DashboardName: str = ...,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...

class InsightRule:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html"""

    Arn: Final[str]

    RuleName: Final[str]

    Ref: Final[str]
    def __init__(
        self,
        *,
        RuleBody: str,
        RuleName: str,
        RuleState: str,
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
