




class RelaunchMerchantFailedTransferArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.IdempotencyKey = None
            self.TransferId = None
            self.MerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.IdempotencyKey = getattr(obj, 'IdempotencyKey', None)
            self.TransferId = getattr(obj, 'TransferId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


