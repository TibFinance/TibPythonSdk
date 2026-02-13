


from ..objects import GetBoardingMerchantStatusEntity
from ..objects import TransactionMailingInfo
from ..objects import ProviderAccount


class GetBoardingMerchantStatusArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.GetBoardingMerchantStatusEntity = None
            self.MailingInfo = None
            self.ProviderCredentials = None

        else:
            
            self.GetBoardingMerchantStatusEntity = GetBoardingMerchantStatusEntity(getattr(obj, 'GetBoardingMerchantStatusEntity', None)) if getattr(obj, 'GetBoardingMerchantStatusEntity', None) is not None else None
            self.MailingInfo = TransactionMailingInfo(getattr(obj, 'MailingInfo', None)) if getattr(obj, 'MailingInfo', None) is not None else None

            self.ProviderCredentials = []
            if hasattr(obj, 'ProviderCredentials') and obj.ProviderCredentials is not None:
                self.ProviderCredentials = [ProviderAccount(name) for name in  obj.ProviderCredentials]


