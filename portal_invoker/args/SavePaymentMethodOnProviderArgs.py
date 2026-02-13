


from ..objects import ProviderAccount
from ..enums import Currency


class SavePaymentMethodOnProviderArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.HostedPaymentToken = None
            self.ProviderCredentials = None
            self.Currency = None
            self.MerchantId = None
            self.CustomerFirstName = None
            self.CustomerLastName = None
            self.ZipCode = None

        else:
            
            self.HostedPaymentToken = getattr(obj, 'HostedPaymentToken', None)

            self.ProviderCredentials = []
            if hasattr(obj, 'ProviderCredentials') and obj.ProviderCredentials is not None:
                self.ProviderCredentials = [ProviderAccount(name) for name in  obj.ProviderCredentials]
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.CustomerFirstName = getattr(obj, 'CustomerFirstName', None)
            self.CustomerLastName = getattr(obj, 'CustomerLastName', None)
            self.ZipCode = getattr(obj, 'ZipCode', None)


