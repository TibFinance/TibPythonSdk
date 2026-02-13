

from .GetBoardingMerchantStatusEntity import GetBoardingMerchantStatusEntity


class GetBoardingMerchantStatusBlueSnapEntity(GetBoardingMerchantStatusEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.MerchantId = None

        else:
            super().__init__(obj)

            self.MerchantId = getattr(obj, 'MerchantId', None)


