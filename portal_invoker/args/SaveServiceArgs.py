


from ..objects import Service


class SaveServiceArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.Service = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.Service = Service(getattr(obj, 'Service', None)) if getattr(obj, 'Service', None) is not None else None


