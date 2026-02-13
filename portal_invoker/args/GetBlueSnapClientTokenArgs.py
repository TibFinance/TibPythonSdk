


from ..objects import ProviderAccount
from ..enums import Currency
from ..objects import TransactionMailingInfo


class GetBlueSnapClientTokenArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ProviderCredentials = None
            self.Currency = None
            self.MerchantId = None
            self.MailingInfo = None

        else:
            

            self.ProviderCredentials = []
            if hasattr(obj, 'ProviderCredentials') and obj.ProviderCredentials is not None:
                self.ProviderCredentials = [ProviderAccount(name) for name in  obj.ProviderCredentials]
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.MailingInfo = TransactionMailingInfo(getattr(obj, 'MailingInfo', None)) if getattr(obj, 'MailingInfo', None) is not None else None


