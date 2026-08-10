
from ..utility import to_enum
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
            self.PaymentId = getattr(obj, 'PaymentId', None)
            self.AutoSelectPaymentFlowResult = to_enum(PaymentFlow, getattr(obj, 'AutoSelectPaymentFlowResult', None))
            self.PaymentFlowParsingResult = to_enum(PaymentFlowParsingResult, getattr(obj, 'PaymentFlowParsingResult', None))
            self.PaymentLink = getattr(obj, 'PaymentLink', None)


