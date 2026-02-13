

from .BaseApiResponse import BaseApiResponse
from ..objects import DasPaymentCanada
from ..objects import DasPaymentQuebec


class ListDasPaymentsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CanadaDasPayments = None
            self.QuebecDasPayments = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.CanadaDasPayments = []
                if hasattr(obj, 'CanadaDasPayments') and obj.CanadaDasPayments is not None:
                    self.CanadaDasPayments = [DasPaymentCanada(name) for name in  obj.CanadaDasPayments]

                self.QuebecDasPayments = []
                if hasattr(obj, 'QuebecDasPayments') and obj.QuebecDasPayments is not None:
                    self.QuebecDasPayments = [DasPaymentQuebec(name) for name in  obj.QuebecDasPayments]


