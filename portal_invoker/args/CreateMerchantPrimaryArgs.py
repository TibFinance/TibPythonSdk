


from ..objects import Merchant


class CreateMerchantPrimaryArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ServiceId = None
            self.MerchantInfo = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.MerchantInfo = Merchant(getattr(obj, 'MerchantInfo', None)) if getattr(obj, 'MerchantInfo', None) is not None else None


