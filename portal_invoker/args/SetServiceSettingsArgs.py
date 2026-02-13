


from ..objects import ServiceSettings


class SetServiceSettingsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.ServiceId = None
            self.Settings = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.Settings = ServiceSettings(getattr(obj, 'Settings', None)) if getattr(obj, 'Settings', None) is not None else None


