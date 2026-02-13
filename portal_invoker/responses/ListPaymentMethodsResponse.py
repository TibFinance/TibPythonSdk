

from .BaseApiResponse import BaseApiResponse
from ..objects import PaymentMethod


class ListPaymentMethodsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.PaymentMethods = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.PaymentMethods = []
                if hasattr(obj, 'PaymentMethods') and obj.PaymentMethods is not None:
                    self.PaymentMethods = [PaymentMethod(name) for name in  obj.PaymentMethods]


