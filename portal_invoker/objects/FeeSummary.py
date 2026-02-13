


from ..enums import OperationKind


class FeeSummary:
    def __init__(self, obj=None):
        if obj is None:
            
            self.TotalFeeAmount = None
            self.TotalFeeCount = None
            self.CreditCardFeesTotal = None
            self.CreditCardFeesCount = None
            self.DirectAccountFeesTotal = None
            self.DirectAccountFeesCount = None
            self.InteracFeesTotal = None
            self.InteracFeesCount = None
            self.FeesByType = None

        else:
            
            self.TotalFeeAmount = getattr(obj, 'TotalFeeAmount', None)
            self.TotalFeeCount = getattr(obj, 'TotalFeeCount', None)
            self.CreditCardFeesTotal = getattr(obj, 'CreditCardFeesTotal', None)
            self.CreditCardFeesCount = getattr(obj, 'CreditCardFeesCount', None)
            self.DirectAccountFeesTotal = getattr(obj, 'DirectAccountFeesTotal', None)
            self.DirectAccountFeesCount = getattr(obj, 'DirectAccountFeesCount', None)
            self.InteracFeesTotal = getattr(obj, 'InteracFeesTotal', None)
            self.InteracFeesCount = getattr(obj, 'InteracFeesCount', None)

            self.FeesByType = []
            if hasattr(obj, 'FeesByType') and obj.FeesByType is not None:
                self.FeesByType = [OperationKind(name) for name in  obj.FeesByType]


