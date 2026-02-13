

from .BaseApiResponse import BaseApiResponse
from ..objects import MerchantView


class CreateSupplierTransferResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.MatchingExistingMerchants = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.MatchingExistingMerchants = []
                if hasattr(obj, 'MatchingExistingMerchants') and obj.MatchingExistingMerchants is not None:
                    self.MatchingExistingMerchants = [MerchantView(name) for name in  obj.MatchingExistingMerchants]


