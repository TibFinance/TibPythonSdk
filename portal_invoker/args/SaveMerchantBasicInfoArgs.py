


from ..objects import MerchantBasicInfo


class SaveMerchantBasicInfoArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.MerchantInfo = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.MerchantInfo = MerchantBasicInfo(getattr(obj, 'MerchantInfo', None)) if getattr(obj, 'MerchantInfo', None) is not None else None


