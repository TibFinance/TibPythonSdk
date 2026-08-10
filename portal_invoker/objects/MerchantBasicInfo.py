
from ..utility import to_enum

from ..enums import Currency
from ..enums import Language


class MerchantBasicInfo:
    def __init__(self, obj=None):
        if obj is None:
            
            self.MerchantName = None
            self.ExternalSystemId = None
            self.ExternalSystemGroupId = None
            self.MerchantCurrency = None
            self.Language = None
            self.Email = None
            self.EmailCopyTo = None
            self.PhoneNumber = None
            self.MerchantDescription = None
            self.Address = None

        else:
            
            from .Address import Address
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.ExternalSystemId = getattr(obj, 'ExternalSystemId', None)
            self.ExternalSystemGroupId = getattr(obj, 'ExternalSystemGroupId', None)
            self.MerchantCurrency = to_enum(Currency, getattr(obj, 'MerchantCurrency', None))
            self.Language = to_enum(Language, getattr(obj, 'Language', None))
            self.Email = getattr(obj, 'Email', None)
            self.EmailCopyTo = getattr(obj, 'EmailCopyTo', None)
            self.PhoneNumber = getattr(obj, 'PhoneNumber', None)
            self.MerchantDescription = getattr(obj, 'MerchantDescription', None)
            self.Address = Address(getattr(obj, 'Address', None)) if getattr(obj, 'Address', None) is not None else None


