

from .BaseApiResponse import BaseApiResponse
from ..objects import PaymentMethodAddRequest
from ..objects import WhiteLabeling


class GetPaymentMethodRequestResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.PaymentMethodRequestData = None
            self.WhiteLabeling = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.PaymentMethodRequestData = PaymentMethodAddRequest(getattr(obj, 'PaymentMethodRequestData', None)) if getattr(obj, 'PaymentMethodRequestData', None) is not None else None
                self.WhiteLabeling = WhiteLabeling(getattr(obj, 'WhiteLabeling', None)) if getattr(obj, 'WhiteLabeling', None) is not None else None


