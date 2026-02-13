




class GetLoginAccesListArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ClientId = None
            self.Username = None
            self.Password = None

        else:
            
            self.ClientId = getattr(obj, 'ClientId', None)
            self.Username = getattr(obj, 'Username', None)
            self.Password = getattr(obj, 'Password', None)


