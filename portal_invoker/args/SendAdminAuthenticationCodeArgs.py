




class SendAdminAuthenticationCodeArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminCode = None

        else:
            
            self.AdminCode = getattr(obj, 'AdminCode', None)


