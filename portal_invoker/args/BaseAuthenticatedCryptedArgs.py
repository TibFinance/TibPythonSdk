




class BaseAuthenticatedCryptedArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)


