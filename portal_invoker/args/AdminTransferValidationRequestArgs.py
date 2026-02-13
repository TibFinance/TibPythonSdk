




class AdminTransferValidationRequestArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.Approved = None
            self.PublicTokenId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.Approved = getattr(obj, 'Approved', None)
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)


