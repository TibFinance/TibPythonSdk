

from .BaseApiResponse import BaseApiResponse
from ..objects import PaymentMethodAddRequest
from ..objects import MerchantView


class GetExternalSupplierFinancialInformationsRequestResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.PaymentMethodRequestData = None
            self.MerchantInfo = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.PaymentMethodRequestData = PaymentMethodAddRequest(getattr(obj, 'PaymentMethodRequestData', None)) if getattr(obj, 'PaymentMethodRequestData', None) is not None else None
                self.MerchantInfo = MerchantView(getattr(obj, 'MerchantInfo', None)) if getattr(obj, 'MerchantInfo', None) is not None else None


