




class GetFeeCountArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.Month = None
            self.Year = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.Month = getattr(obj, 'Month', None)
            self.Year = getattr(obj, 'Year', None)


