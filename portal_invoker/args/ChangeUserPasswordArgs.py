




class ChangeUserPasswordArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.Password = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.Password = getattr(obj, 'Password', None)


