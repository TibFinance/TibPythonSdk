




class GetTokenInformationArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)


