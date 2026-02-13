

from .BaseApiResponse import BaseApiResponse
from ..objects import MerchantFee


class GetFeeCountResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.TransactionFeesAgregated = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.TransactionFeesAgregated = []
                if hasattr(obj, 'TransactionFeesAgregated') and obj.TransactionFeesAgregated is not None:
                    self.TransactionFeesAgregated = [MerchantFee(name) for name in  obj.TransactionFeesAgregated]


