




class ProviderMerchantCredentialEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.UserName = None
            self.Password = None
            self.DataProtectionKey = None
            self.MerchantId = None

        else:
            
            self.UserName = getattr(obj, 'UserName', None)
            self.Password = getattr(obj, 'Password', None)
            self.DataProtectionKey = getattr(obj, 'DataProtectionKey', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


