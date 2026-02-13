




class CreateManualRefundForTransferOperationArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.TransferId = None
            self.MerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.TransferId = getattr(obj, 'TransferId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


