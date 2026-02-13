


from ..objects import ServiceSettings


class SetClientDefaultServiceSettingsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.ClientId = None
            self.Settings = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.Settings = ServiceSettings(getattr(obj, 'Settings', None)) if getattr(obj, 'Settings', None) is not None else None


