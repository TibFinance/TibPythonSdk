

from .BaseApiResponse import BaseApiResponse
from ..objects import Payment


class GetPaymentResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Payment = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Payment = Payment(getattr(obj, 'Payment', None)) if getattr(obj, 'Payment', None) is not None else None


