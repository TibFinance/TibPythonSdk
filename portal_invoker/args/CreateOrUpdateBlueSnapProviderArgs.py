




class CreateOrUpdateBlueSnapProviderArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.BsMerchantId = None
            self.BsUsername = None
            self.BsPassword = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.BsMerchantId = getattr(obj, 'BsMerchantId', None)
            self.BsUsername = getattr(obj, 'BsUsername', None)
            self.BsPassword = getattr(obj, 'BsPassword', None)


