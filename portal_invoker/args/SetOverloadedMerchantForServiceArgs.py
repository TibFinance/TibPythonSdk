




class SetOverloadedMerchantForServiceArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.ServiceId = None
            self.FeesOverLoadMerchantId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.FeesOverLoadMerchantId = getattr(obj, 'FeesOverLoadMerchantId', None)


