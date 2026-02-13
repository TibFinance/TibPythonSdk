

from .DasPaymentQuebecEntity import DasPaymentQuebecEntity
from ..enums import DasPaymentProcessStatus


class DasPaymentQuebec(DasPaymentQuebecEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.PaymentId = None
            self.Status = None

        else:
            super().__init__(obj)

            self.PaymentId = getattr(obj, 'PaymentId', None)
            self.Status = DasPaymentProcessStatus(getattr(obj, 'Status', None)) if getattr(obj, 'Status', None) is not None else None


