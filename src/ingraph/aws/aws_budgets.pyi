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

_NAMESPACE = "AWS::Budgets"

class Budget:
    """Documentation: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html"""

    Ref: Final[str]
    def __init__(
        self,
        *,
        Budget: "Budget.BudgetData",
        DeletionPolicy: str = ...,
        DependsOn: List[Any] = ...,
        NotificationsWithSubscribers: List["Budget.NotificationWithSubscribers"] = ...,
        UpdateReplacePolicy: str = ...
    ): ...
    class BudgetData:
        def __init__(
            self,
            *,
            BudgetType: str,
            TimeUnit: str,
            BudgetLimit: "Budget.Spend" = ...,
            BudgetName: str = ...,
            CostFilters: Any = ...,
            CostTypes: "Budget.CostTypes" = ...,
            PlannedBudgetLimits: Any = ...,
            TimePeriod: "Budget.TimePeriod" = ...
        ): ...
    class CostTypes:
        def __init__(
            self,
            *,
            IncludeCredit: bool = ...,
            IncludeDiscount: bool = ...,
            IncludeOtherSubscription: bool = ...,
            IncludeRecurring: bool = ...,
            IncludeRefund: bool = ...,
            IncludeSubscription: bool = ...,
            IncludeSupport: bool = ...,
            IncludeTax: bool = ...,
            IncludeUpfront: bool = ...,
            UseAmortized: bool = ...,
            UseBlended: bool = ...
        ): ...
    class Notification:
        def __init__(
            self,
            *,
            ComparisonOperator: str,
            NotificationType: str,
            Threshold: float,
            ThresholdType: str = ...
        ): ...
    class NotificationWithSubscribers:
        def __init__(
            self,
            *,
            Notification: "Budget.Notification",
            Subscribers: List["Budget.Subscriber"]
        ): ...
    class Spend:
        def __init__(self, *, Amount: float, Unit: str): ...
    class Subscriber:
        def __init__(self, *, Address: str, SubscriptionType: str): ...
    class TimePeriod:
        def __init__(self, *, End: str = ..., Start: str = ...): ...
