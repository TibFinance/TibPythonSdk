




class UpdateClientArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.ClientId = None
            self.ClientName = None
            self.FeesOverloadedMerchantId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.ClientName = getattr(obj, 'ClientName', None)
            self.FeesOverloadedMerchantId = getattr(obj, 'FeesOverloadedMerchantId', None)


