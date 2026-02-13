


from ..objects import ServiceFeeSettings


class SetClientDefaultServiceFeeSettingsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ClientId = None
            self.ServiceFeeSettings = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.ServiceFeeSettings = ServiceFeeSettings(getattr(obj, 'ServiceFeeSettings', None)) if getattr(obj, 'ServiceFeeSettings', None) is not None else None


