




class TransactionFeesAgregated:
    def __init__(self, obj=None):
        if obj is None:
            
            self.FeesByCount = None
            self.TotalFeeAmount = None
            self.TotalNumberOfPayments = None
            self.TotalNumberOfFees = None

        else:
            
            from .TransactionFeesForCount import TransactionFeesForCount

            self.FeesByCount = []
            if hasattr(obj, 'FeesByCount') and obj.FeesByCount is not None:
                self.FeesByCount = [TransactionFeesForCount(name) for name in  obj.FeesByCount]
            self.TotalFeeAmount = getattr(obj, 'TotalFeeAmount', None)
            self.TotalNumberOfPayments = getattr(obj, 'TotalNumberOfPayments', None)
            self.TotalNumberOfFees = getattr(obj, 'TotalNumberOfFees', None)


