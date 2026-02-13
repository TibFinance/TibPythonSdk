




class TransactionFeesForCount:
    def __init__(self, obj=None):
        if obj is None:
            
            self.FeeCount = None
            self.FeeAmount = None
            self.NumberOfPayment = None
            self.NumberOfFees = None

        else:
            
            self.FeeCount = getattr(obj, 'FeeCount', None)
            self.FeeAmount = getattr(obj, 'FeeAmount', None)
            self.NumberOfPayment = getattr(obj, 'NumberOfPayment', None)
            self.NumberOfFees = getattr(obj, 'NumberOfFees', None)


