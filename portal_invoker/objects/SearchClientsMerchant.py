




class SearchClientsMerchant:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ClientId = None
            self.ClientName = None
            self.ClientIsDeleted = None
            self.ServiceId = None
            self.ServiceName = None
            self.ServiceIsDeleted = None
            self.MerchantId = None
            self.MerchantName = None
            self.MerchantIsDeleted = None

        else:
            
            self.ClientId = getattr(obj, 'ClientId', None)
            self.ClientName = getattr(obj, 'ClientName', None)
            self.ClientIsDeleted = getattr(obj, 'ClientIsDeleted', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.ServiceName = getattr(obj, 'ServiceName', None)
            self.ServiceIsDeleted = getattr(obj, 'ServiceIsDeleted', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.MerchantIsDeleted = getattr(obj, 'MerchantIsDeleted', None)


