




class MerchantIdName:
    def __init__(self, obj=None):
        if obj is None:
            
            self.MerchantId = None
            self.MerchantName = None

        else:
            
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)


