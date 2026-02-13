

from .BaseApiResponse import BaseApiResponse
from ..objects import AggregatedCategoryExtraction
from ..objects import MonthlyStats
from ..objects import CashBackStats


class GetSummaryInformationsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.AggregatedCategoryExtractions = None
            self.MonthlyTransactionStats = None
            self.DailyCashbackStats = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.AggregatedCategoryExtractions = []
                if hasattr(obj, 'AggregatedCategoryExtractions') and obj.AggregatedCategoryExtractions is not None:
                    self.AggregatedCategoryExtractions = [AggregatedCategoryExtraction(name) for name in  obj.AggregatedCategoryExtractions]

                self.MonthlyTransactionStats = []
                if hasattr(obj, 'MonthlyTransactionStats') and obj.MonthlyTransactionStats is not None:
                    self.MonthlyTransactionStats = [MonthlyStats(name) for name in  obj.MonthlyTransactionStats]

                self.DailyCashbackStats = []
                if hasattr(obj, 'DailyCashbackStats') and obj.DailyCashbackStats is not None:
                    self.DailyCashbackStats = [CashBackStats(name) for name in  obj.DailyCashbackStats]


