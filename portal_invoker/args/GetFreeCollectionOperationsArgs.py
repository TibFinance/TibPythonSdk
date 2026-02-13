




class GetFreeCollectionOperationsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.FromDate = None
            self.ToDate = None
            self.TransferGroupId = None
            self.OnlyWithErrors = None
            self.MerchantId = None
            self.ServiceId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.FromDate = getattr(obj, 'FromDate', None)
            self.ToDate = getattr(obj, 'ToDate', None)
            self.TransferGroupId = getattr(obj, 'TransferGroupId', None)
            self.OnlyWithErrors = getattr(obj, 'OnlyWithErrors', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)


