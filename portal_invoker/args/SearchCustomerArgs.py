




class SearchCustomerArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.CustomerName = None
            self.MerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.CustomerName = getattr(obj, 'CustomerName', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


