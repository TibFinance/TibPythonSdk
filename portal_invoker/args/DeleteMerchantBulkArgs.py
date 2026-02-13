




class DeleteMerchantBulkArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.MerchantIds = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)

            self.MerchantIds = []
            if hasattr(obj, 'MerchantIds') and obj.MerchantIds is not None:
                self.MerchantIds = [name for name in obj.MerchantIds]


