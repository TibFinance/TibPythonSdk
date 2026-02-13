


from ..objects import GetBoardingMerchantCredentialEntity
from ..objects import TransactionMailingInfo
from ..objects import ProviderAccount


class GetBoardingMerchantCredentialArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.GetBoardingMerchantCredentialEntity = None
            self.MailingInfo = None
            self.ProviderCredentials = None

        else:
            
            self.GetBoardingMerchantCredentialEntity = GetBoardingMerchantCredentialEntity(getattr(obj, 'GetBoardingMerchantCredentialEntity', None)) if getattr(obj, 'GetBoardingMerchantCredentialEntity', None) is not None else None
            self.MailingInfo = TransactionMailingInfo(getattr(obj, 'MailingInfo', None)) if getattr(obj, 'MailingInfo', None) is not None else None

            self.ProviderCredentials = []
            if hasattr(obj, 'ProviderCredentials') and obj.ProviderCredentials is not None:
                self.ProviderCredentials = [ProviderAccount(name) for name in  obj.ProviderCredentials]


