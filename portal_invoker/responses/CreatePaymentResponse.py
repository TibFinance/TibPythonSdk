

from .BaseApiResponse import BaseApiResponse
from ..enums import PaymentFlow
from ..enums import PaymentFlowParsingResult


class CreatePaymentResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.PaymentId = None
            self.AutoSelectPaymentFlowResult = None
            self.PaymentFlowParsingResult = None
            self.PaymentLink = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.PaymentId = getattr(obj, 'PaymentId', None)
                self.AutoSelectPaymentFlowResult = PaymentFlow(getattr(obj, 'AutoSelectPaymentFlowResult', None)) if getattr(obj, 'AutoSelectPaymentFlowResult', None) is not None else None
                self.PaymentFlowParsingResult = PaymentFlowParsingResult(getattr(obj, 'PaymentFlowParsingResult', None)) if getattr(obj, 'PaymentFlowParsingResult', None) is not None else None
                self.PaymentLink = getattr(obj, 'PaymentLink', None)


