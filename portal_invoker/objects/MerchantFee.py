




class MerchantFee:
    def __init__(self, obj=None):
        if obj is None:
            
            self.MerchantId = None
            self.MerchantFees = None

        else:
            
            from .TransactionFeesAgregated import TransactionFeesAgregated
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.MerchantFees = TransactionFeesAgregated(getattr(obj, 'MerchantFees', None)) if getattr(obj, 'MerchantFees', None) is not None else None


