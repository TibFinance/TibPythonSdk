




class CreateCustomerFromMerchantArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.MerchantId = None
            self.ClientId = None
            self.ServiceId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)


