




class TransferValidationRequestArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.Approved = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.Approved = getattr(obj, 'Approved', None)


