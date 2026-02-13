




class MoveMerchantArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.MerchantdId = None
            self.ServiceId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.MerchantdId = getattr(obj, 'MerchantdId', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)


