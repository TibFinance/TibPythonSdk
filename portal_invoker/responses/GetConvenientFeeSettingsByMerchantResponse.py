

from .BaseApiResponse import BaseApiResponse
from ..objects import ConvenientFeeSettings


class GetConvenientFeeSettingsByMerchantResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ConvenientFeeSettings = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.ConvenientFeeSettings = []
                if hasattr(obj, 'ConvenientFeeSettings') and obj.ConvenientFeeSettings is not None:
                    self.ConvenientFeeSettings = [ConvenientFeeSettings(name) for name in  obj.ConvenientFeeSettings]


