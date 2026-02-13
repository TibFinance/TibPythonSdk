




class LoginAdminArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.LoginsUserRelationsId = None
            self.ClientId = None
            self.Username = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.LoginsUserRelationsId = getattr(obj, 'LoginsUserRelationsId', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.Username = getattr(obj, 'Username', None)


