




class MerchantEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.MerchantId = None
            self.ServiceId = None
            self.MerchantName = None
            self.MerchantEmail = None
            self.IsClientMerchant = None
            self.Language = None

        else:
            
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.MerchantEmail = getattr(obj, 'MerchantEmail', None)
            self.IsClientMerchant = getattr(obj, 'IsClientMerchant', None)
            self.Language = getattr(obj, 'Language', None)


