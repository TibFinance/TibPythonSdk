


from ..enums import ValidationLimitStatus
from ..enums import TibAuthorizationStatus
from ..enums import ClientAuthorizationStatus


class ValidationLimitsContainer:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ServiceId = None
            self.LimitStatus = None
            self.TibAuthorization = None
            self.ClientAuthorization = None
            self.TibMessages = None
            self.ClientMessages = None

        else:
            
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.LimitStatus = ValidationLimitStatus(getattr(obj, 'LimitStatus', None)) if getattr(obj, 'LimitStatus', None) is not None else None
            self.TibAuthorization = TibAuthorizationStatus(getattr(obj, 'TibAuthorization', None)) if getattr(obj, 'TibAuthorization', None) is not None else None
            self.ClientAuthorization = ClientAuthorizationStatus(getattr(obj, 'ClientAuthorization', None)) if getattr(obj, 'ClientAuthorization', None) is not None else None

            self.TibMessages = []
            if hasattr(obj, 'TibMessages') and obj.TibMessages is not None:
                self.TibMessages = [name for name in obj.TibMessages]

            self.ClientMessages = []
            if hasattr(obj, 'ClientMessages') and obj.ClientMessages is not None:
                self.ClientMessages = [name for name in obj.ClientMessages]


