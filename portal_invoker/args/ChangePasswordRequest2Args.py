




class ChangePasswordRequest2Args:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ClientId = None
            self.Username = None

        else:
            
            self.ClientId = getattr(obj, 'ClientId', None)
            self.Username = getattr(obj, 'Username', None)


