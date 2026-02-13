

from .BaseApiResponse import BaseApiResponse
from ..objects import Customer


class GetCustomerResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Customer = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Customer = Customer(getattr(obj, 'Customer', None)) if getattr(obj, 'Customer', None) is not None else None


