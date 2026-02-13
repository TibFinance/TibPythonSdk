




class DeleteMerchantForAdminArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.MerchantId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


