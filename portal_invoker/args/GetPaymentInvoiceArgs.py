


from ..objects import ProviderAccount
from ..enums import Currency


class GetPaymentInvoiceArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ProviderCredentials = None
            self.Currency = None
            self.MerchantId = None
            self.FromDate = None
            self.ToDate = None

        else:
            

            self.ProviderCredentials = []
            if hasattr(obj, 'ProviderCredentials') and obj.ProviderCredentials is not None:
                self.ProviderCredentials = [ProviderAccount(name) for name in  obj.ProviderCredentials]
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.FromDate = getattr(obj, 'FromDate', None)
            self.ToDate = getattr(obj, 'ToDate', None)


