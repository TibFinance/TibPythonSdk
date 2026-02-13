

from .BaseApiResponse import BaseApiResponse
from ..objects import PaymentMethod


class GetPaymentMethodResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.PaymentMethod = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.PaymentMethod = PaymentMethod(getattr(obj, 'PaymentMethod', None)) if getattr(obj, 'PaymentMethod', None) is not None else None


