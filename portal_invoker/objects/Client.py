

from .ClientEntity import ClientEntity


class Client(ClientEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ClientId = None
            self.WhiteLabelingId = None

        else:
            super().__init__(obj)

            self.ClientId = getattr(obj, 'ClientId', None)

            self.WhiteLabelingId = []
            if hasattr(obj, 'WhiteLabelingId') and obj.WhiteLabelingId is not None:
                self.WhiteLabelingId = [name for name in obj.WhiteLabelingId]


