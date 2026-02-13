




class CreateMerchantLoginArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.Email = None
            self.FirstName = None
            self.LastName = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.Email = getattr(obj, 'Email', None)
            self.FirstName = getattr(obj, 'FirstName', None)
            self.LastName = getattr(obj, 'LastName', None)


