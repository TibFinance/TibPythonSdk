




class CollectMerchantArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.MerchantId = None
            self.Amount = None
            self.OperationKind = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.OperationKind = getattr(obj, 'OperationKind', None)


