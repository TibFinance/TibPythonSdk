

from .BaseApiResponse import BaseApiResponse
from ..objects import ClientWithRequestCount


class ListClientsWithRequestCountResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Clients = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.Clients = []
                if hasattr(obj, 'Clients') and obj.Clients is not None:
                    self.Clients = [ClientWithRequestCount(name) for name in  obj.Clients]


