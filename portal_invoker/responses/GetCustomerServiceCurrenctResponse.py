

from .BaseApiResponse import BaseApiResponse


class GetCustomerServiceCurrenctResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Currency = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Currency = getattr(obj, 'Currency', None)


