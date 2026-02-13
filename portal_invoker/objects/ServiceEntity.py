


from ..enums import Language
from ..enums import Provider
from ..enums import Currency


class ServiceEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ServiceName = None
            self.DefaultCustomerLanguage = None
            self.ProviderType = None
            self.Currency = None

        else:
            
            self.ServiceName = getattr(obj, 'ServiceName', None)
            self.DefaultCustomerLanguage = Language(getattr(obj, 'DefaultCustomerLanguage', None)) if getattr(obj, 'DefaultCustomerLanguage', None) is not None else None
            self.ProviderType = Provider(getattr(obj, 'ProviderType', None)) if getattr(obj, 'ProviderType', None) is not None else None
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None


