




class GetTransferCreationListArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ServiceId = None
            self.MerchantId = None
            self.TransferType = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.TransferType = getattr(obj, 'TransferType', None)


