




class BaseProcessDropInArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.IsPPAAuthorized = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.IsPPAAuthorized = getattr(obj, 'IsPPAAuthorized', None)


