

from .GetBoardingMerchantCredentialEntity import GetBoardingMerchantCredentialEntity


class GetBoardingMerchantCredentialBlueSnapEntity(GetBoardingMerchantCredentialEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ProviderMerchantId = None

        else:
            super().__init__(obj)

            self.ProviderMerchantId = getattr(obj, 'ProviderMerchantId', None)


