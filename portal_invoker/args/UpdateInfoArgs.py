




class UpdateInfoArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.MerchantId = None
            self.ClientName = None
            self.ServiceName = None
            self.MerchantName = None
            self.AccountName = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.ClientName = getattr(obj, 'ClientName', None)
            self.ServiceName = getattr(obj, 'ServiceName', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.AccountName = getattr(obj, 'AccountName', None)


