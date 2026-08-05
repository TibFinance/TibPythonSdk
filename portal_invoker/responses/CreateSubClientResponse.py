

from .BaseApiResponse import BaseApiResponse


class CreateSubClientResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ServiceId = None
            self.BoardingRedirectUrl = None

        else:
            super().__init__(obj)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.BoardingRedirectUrl = getattr(obj, 'BoardingRedirectUrl', None)


