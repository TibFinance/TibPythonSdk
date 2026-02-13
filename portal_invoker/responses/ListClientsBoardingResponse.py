

from .BaseApiResponse import BaseApiResponse
from ..objects import ClientBoarding


class ListClientsBoardingResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Clients = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.Clients = []
                if hasattr(obj, 'Clients') and obj.Clients is not None:
                    self.Clients = [ClientBoarding(name) for name in  obj.Clients]


