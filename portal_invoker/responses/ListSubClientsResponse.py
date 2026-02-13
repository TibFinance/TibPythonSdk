

from .BaseApiResponse import BaseApiResponse
from ..objects import Service


class ListSubClientsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Services = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.Services = []
                if hasattr(obj, 'Services') and obj.Services is not None:
                    self.Services = [Service(name) for name in  obj.Services]


