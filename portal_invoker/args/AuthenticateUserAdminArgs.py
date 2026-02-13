




class AuthenticateUserAdminArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.ClientId = None
            self.UserName = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.UserName = getattr(obj, 'UserName', None)


