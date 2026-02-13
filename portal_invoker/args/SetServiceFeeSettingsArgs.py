


from ..objects import ServiceFeeSettings


class SetServiceFeeSettingsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ServiceId = None
            self.ServiceFeeSettings = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.ServiceFeeSettings = ServiceFeeSettings(getattr(obj, 'ServiceFeeSettings', None)) if getattr(obj, 'ServiceFeeSettings', None) is not None else None


