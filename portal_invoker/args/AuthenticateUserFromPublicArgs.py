




class AuthenticateUserFromPublicArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ClientId = None
            self.Username = None
            self.Password = None
            self.IpAddress = None

        else:
            
            self.ClientId = getattr(obj, 'ClientId', None)
            self.Username = getattr(obj, 'Username', None)
            self.Password = getattr(obj, 'Password', None)
            self.IpAddress = getattr(obj, 'IpAddress', None)


