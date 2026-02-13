


from ..enums import DataSummaryAggregationCategory


class AggregatedCategoryExtraction:
    def __init__(self, obj=None):
        if obj is None:
            
            self.DataSummaryAggregationCategory = None
            self.Count = None
            self.Amount = None

        else:
            
            self.DataSummaryAggregationCategory = DataSummaryAggregationCategory(getattr(obj, 'DataSummaryAggregationCategory', None)) if getattr(obj, 'DataSummaryAggregationCategory', None) is not None else None
            self.Count = getattr(obj, 'Count', None)
            self.Amount = getattr(obj, 'Amount', None)


