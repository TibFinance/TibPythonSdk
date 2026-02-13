

from .BaseApiResponse import BaseApiResponse
from ..objects import GetBoardingMerchantCredentialResultEntity


class GetBoardingMerchantCredentialResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.GetBoardingMerchantCredentialResultEntity = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.GetBoardingMerchantCredentialResultEntity = GetBoardingMerchantCredentialResultEntity(getattr(obj, 'GetBoardingMerchantCredentialResultEntity', None)) if getattr(obj, 'GetBoardingMerchantCredentialResultEntity', None) is not None else None


