




class GetFeesOverloadMerchantArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.Id = None
            self.Source = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.Id = getattr(obj, 'Id', None)
            self.Source = getattr(obj, 'Source', None)


