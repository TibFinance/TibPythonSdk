

from .BaseApiResponse import BaseApiResponse
from ..objects import MerchantView


class GetMerchantResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Merchant = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Merchant = MerchantView(getattr(obj, 'Merchant', None)) if getattr(obj, 'Merchant', None) is not None else None


