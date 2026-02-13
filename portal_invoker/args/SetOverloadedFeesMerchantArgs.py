




class SetOverloadedFeesMerchantArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ServiceId = None
            self.OverloadedMerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.OverloadedMerchantId = getattr(obj, 'OverloadedMerchantId', None)


