
from ..utility import to_enum

from ..enums import Language
from ..enums import Currency


class ServiceEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ServiceName = None
            self.DefaultCustomerLanguage = None
            self.Currency = None

        else:
            
            self.ServiceName = getattr(obj, 'ServiceName', None)
            self.DefaultCustomerLanguage = to_enum(Language, getattr(obj, 'DefaultCustomerLanguage', None))
            self.Currency = to_enum(Currency, getattr(obj, 'Currency', None))


