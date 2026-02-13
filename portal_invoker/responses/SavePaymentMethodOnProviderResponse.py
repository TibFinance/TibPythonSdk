

from .BaseApiResponse import BaseApiResponse
from ..objects import SavePaymentMethodResultEntity


class SavePaymentMethodOnProviderResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.SavePaymentMethodResultEntity = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.SavePaymentMethodResultEntity = SavePaymentMethodResultEntity(getattr(obj, 'SavePaymentMethodResultEntity', None)) if getattr(obj, 'SavePaymentMethodResultEntity', None) is not None else None


