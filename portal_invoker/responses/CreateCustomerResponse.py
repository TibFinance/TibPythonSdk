

from .BaseApiResponse import BaseApiResponse


class CreateCustomerResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CustomerId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.CustomerId = getattr(obj, 'CustomerId', None)


