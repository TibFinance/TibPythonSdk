

from .BaseApiResponse import BaseApiResponse
from ..objects import GetBoardingMerchantStatusResultEntity


class GetBoardingMerchantStatusResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.GetBoardingStatusResultEntity = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.GetBoardingStatusResultEntity = GetBoardingMerchantStatusResultEntity(getattr(obj, 'GetBoardingStatusResultEntity', None)) if getattr(obj, 'GetBoardingStatusResultEntity', None) is not None else None


