

from .BaseApiResponse import BaseApiResponse
from ..objects import ClientSettings
from ..objects import ServiceSettings
from ..objects import ServiceFeeSettings


class GetClientSettingsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ClientSettings = None
            self.ServiceSettings = None
            self.ServiceFeeSettings = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.ClientSettings = ClientSettings(getattr(obj, 'ClientSettings', None)) if getattr(obj, 'ClientSettings', None) is not None else None
                self.ServiceSettings = ServiceSettings(getattr(obj, 'ServiceSettings', None)) if getattr(obj, 'ServiceSettings', None) is not None else None
                self.ServiceFeeSettings = ServiceFeeSettings(getattr(obj, 'ServiceFeeSettings', None)) if getattr(obj, 'ServiceFeeSettings', None) is not None else None


