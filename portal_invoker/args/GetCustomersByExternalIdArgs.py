




class GetCustomersByExternalIdArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ExternalCustomerId = None
            self.MerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ExternalCustomerId = getattr(obj, 'ExternalCustomerId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


