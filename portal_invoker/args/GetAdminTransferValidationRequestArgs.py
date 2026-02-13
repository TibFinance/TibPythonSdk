




class GetAdminTransferValidationRequestArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.PublicTokenId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)


