




class DeleteLoginArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.LoginId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.LoginId = getattr(obj, 'LoginId', None)


