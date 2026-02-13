


from ..objects import ClientLogin


class CreateClientLoginArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.Password = None
            self.ClientLogin = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.Password = getattr(obj, 'Password', None)
            self.ClientLogin = ClientLogin(getattr(obj, 'ClientLogin', None)) if getattr(obj, 'ClientLogin', None) is not None else None


