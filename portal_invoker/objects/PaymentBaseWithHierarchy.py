




class PaymentBaseWithHierarchy:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ServiceId = None
            self.ServiceName = None
            self.MerchantId = None
            self.MerchantExternalSystemId = None
            self.MerchantExternalSystemGroupId = None
            self.MerchantName = None
            self.IsOverlodedMerchant = None

        else:
            
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.ServiceName = getattr(obj, 'ServiceName', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.MerchantExternalSystemId = getattr(obj, 'MerchantExternalSystemId', None)
            self.MerchantExternalSystemGroupId = getattr(obj, 'MerchantExternalSystemGroupId', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.IsOverlodedMerchant = getattr(obj, 'IsOverlodedMerchant', None)


