

from .BaseApiResponse import BaseApiResponse
from ..objects import ConvenientFeeSettings


class AddOrUpdateConvenientFeeSettingsForMerchantResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ConvenientFeeSettings = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.ConvenientFeeSettings = ConvenientFeeSettings(getattr(obj, 'ConvenientFeeSettings', None)) if getattr(obj, 'ConvenientFeeSettings', None) is not None else None


