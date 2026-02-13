

from .BaseApiResponse import BaseApiResponse


class GetPublicTokenInformationResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ClientId = None
            self.ServiceId = None
            self.ServiceName = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.ClientId = getattr(obj, 'ClientId', None)
                self.ServiceId = getattr(obj, 'ServiceId', None)
                self.ServiceName = getattr(obj, 'ServiceName', None)


