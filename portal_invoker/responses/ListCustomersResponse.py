

from .BaseApiResponse import BaseApiResponse
from ..objects import Customer


class ListCustomersResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Customers = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.Customers = []
                if hasattr(obj, 'Customers') and obj.Customers is not None:
                    self.Customers = [Customer(name) for name in  obj.Customers]


