

from .BaseEventPayload import BaseEventPayload


class BoardingEventPayload(BaseEventPayload):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.MerchantId = None
            self.ServiceId = None
            self.ClientId = None
            self.BoardingStatus = None

        else:
            super().__init__(obj)

            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.BoardingStatus = getattr(obj, 'BoardingStatus', None)


