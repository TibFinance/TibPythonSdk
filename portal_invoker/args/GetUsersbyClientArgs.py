




class GetUsersbyClientArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.ClientId = None
            self.LoginId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.LoginId = getattr(obj, 'LoginId', None)


