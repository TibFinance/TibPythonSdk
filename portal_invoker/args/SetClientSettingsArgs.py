


from ..objects import ClientSettings


class SetClientSettingsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ClientId = None
            self.ClientSettings = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.ClientSettings = ClientSettings(getattr(obj, 'ClientSettings', None)) if getattr(obj, 'ClientSettings', None) is not None else None


