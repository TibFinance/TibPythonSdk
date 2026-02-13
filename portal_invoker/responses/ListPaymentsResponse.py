

from .BaseApiResponse import BaseApiResponse
from ..objects import Payment


class ListPaymentsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Payments = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.Payments = []
                if hasattr(obj, 'Payments') and obj.Payments is not None:
                    self.Payments = [Payment(name) for name in  obj.Payments]


