




class ValidateCompanyInfoArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ClientId = None
            self.ClientName = None

        else:
            
            self.ClientId = getattr(obj, 'ClientId', None)
            self.ClientName = getattr(obj, 'ClientName', None)


