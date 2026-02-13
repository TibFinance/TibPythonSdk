


from ..enums import Currency
from ..enums import Language
from ..enums import Provider


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
            self.FavoriteProvider = None

        else:
            
            from .Address import Address
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.ExternalSystemId = getattr(obj, 'ExternalSystemId', None)
            self.ExternalSystemGroupId = getattr(obj, 'ExternalSystemGroupId', None)
            self.MerchantCurrency = Currency(getattr(obj, 'MerchantCurrency', None)) if getattr(obj, 'MerchantCurrency', None) is not None else None
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.Email = getattr(obj, 'Email', None)
            self.EmailCopyTo = getattr(obj, 'EmailCopyTo', None)
            self.PhoneNumber = getattr(obj, 'PhoneNumber', None)
            self.MerchantDescription = getattr(obj, 'MerchantDescription', None)
            self.Address = Address(getattr(obj, 'Address', None)) if getattr(obj, 'Address', None) is not None else None
            self.FavoriteProvider = Provider(getattr(obj, 'FavoriteProvider', None)) if getattr(obj, 'FavoriteProvider', None) is not None else None


