

from .BaseApiResponse import BaseApiResponse
from ..objects import MerchantView


class GetMerchantsByExternalIdResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Merchants = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.Merchants = []
                if hasattr(obj, 'Merchants') and obj.Merchants is not None:
                    self.Merchants = [MerchantView(name) for name in  obj.Merchants]


