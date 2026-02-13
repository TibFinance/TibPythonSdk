

from .BaseApiResponse import BaseApiResponse
from ..objects import Client


class GetClientResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Client = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Client = Client(getattr(obj, 'Client', None)) if getattr(obj, 'Client', None) is not None else None


