




class CreateClientLoginBoardingArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.Username = None
            self.Password = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.Username = getattr(obj, 'Username', None)
            self.Password = getattr(obj, 'Password', None)


