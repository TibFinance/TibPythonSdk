

from .BaseApiResponse import BaseApiResponse


class CreateCreditCardPaymentMethodResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.PaymentMethodId = None

        else:
            super().__init__(obj)
            self.PaymentMethodId = getattr(obj, 'PaymentMethodId', None)


