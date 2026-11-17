

from .BaseApiResponse import BaseApiResponse


class CreateCustomerV2Response(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CustomerId = None

        else:
            super().__init__(obj)
            self.CustomerId = getattr(obj, 'CustomerId', None)


