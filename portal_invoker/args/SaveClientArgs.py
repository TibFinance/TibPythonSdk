


from ..objects import ClientEntity


class SaveClientArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.Client = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.Client = ClientEntity(getattr(obj, 'Client', None)) if getattr(obj, 'Client', None) is not None else None


