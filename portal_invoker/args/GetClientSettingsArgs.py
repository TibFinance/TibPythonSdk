




class GetClientSettingsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ClientId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ClientId = getattr(obj, 'ClientId', None)


