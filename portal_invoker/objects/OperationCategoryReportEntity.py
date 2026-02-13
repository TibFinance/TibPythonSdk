


from ..enums import OperationCategoryReportType


class OperationCategoryReportEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CategoryType = None
            self.NumberOfTransactions = None
            self.Amount = None
            self.IncludedTransfers = None
            self.IncludedOperations = None

        else:
            
            self.CategoryType = OperationCategoryReportType(getattr(obj, 'CategoryType', None)) if getattr(obj, 'CategoryType', None) is not None else None
            self.NumberOfTransactions = getattr(obj, 'NumberOfTransactions', None)
            self.Amount = getattr(obj, 'Amount', None)

            self.IncludedTransfers = []
            if hasattr(obj, 'IncludedTransfers') and obj.IncludedTransfers is not None:
                self.IncludedTransfers = [name for name in obj.IncludedTransfers]

            self.IncludedOperations = []
            if hasattr(obj, 'IncludedOperations') and obj.IncludedOperations is not None:
                self.IncludedOperations = [name for name in obj.IncludedOperations]


