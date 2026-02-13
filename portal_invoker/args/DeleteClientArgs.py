




class DeleteClientArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)


