




class GetSubClientArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.SubClientId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.SubClientId = getattr(obj, 'SubClientId', None)


