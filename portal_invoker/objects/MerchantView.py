
from ..utility import to_enum

from ..enums import Currency
from ..enums import Language
from ..enums import ProvinceStateId
from ..enums import CountryId
from ..enums import Provider


class MerchantView:
    def __init__(self, obj=None):
        if obj is None:
            
            self.MerchantId = None
            self.MerchantName = None
            self.AccountName = None
            self.AccountPreview = None
            self.ExternalSystemId = None
            self.ExternalSystemGroupId = None
            self.MerchantCurrency = None
            self.MerchantLanguage = None
            self.Email = None
            self.IsAuthorized = None
            self.EmailCopyTo = None
            self.MerchantPhoneNumber = None
            self.StreetAddress = None
            self.AddressCity = None
            self.ProvinceStateId = None
            self.ServiceId = None
            self.CountryId = None
            self.PostalZipCode = None
            self.AccountProvider = None
            self.BoardingStatus = None
            self.BoardingFiles = None

        else:
            
            from .BoardingFile import BoardingFile
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.AccountName = getattr(obj, 'AccountName', None)
            self.AccountPreview = getattr(obj, 'AccountPreview', None)
            self.ExternalSystemId = getattr(obj, 'ExternalSystemId', None)
            self.ExternalSystemGroupId = getattr(obj, 'ExternalSystemGroupId', None)
            self.MerchantCurrency = to_enum(Currency, getattr(obj, 'MerchantCurrency', None))
            self.MerchantLanguage = to_enum(Language, getattr(obj, 'MerchantLanguage', None))
            self.Email = getattr(obj, 'Email', None)
            self.IsAuthorized = getattr(obj, 'IsAuthorized', None)
            self.EmailCopyTo = getattr(obj, 'EmailCopyTo', None)
            self.MerchantPhoneNumber = getattr(obj, 'MerchantPhoneNumber', None)
            self.StreetAddress = getattr(obj, 'StreetAddress', None)
            self.AddressCity = getattr(obj, 'AddressCity', None)
            self.ProvinceStateId = to_enum(ProvinceStateId, getattr(obj, 'ProvinceStateId', None))
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.CountryId = to_enum(CountryId, getattr(obj, 'CountryId', None))
            self.PostalZipCode = getattr(obj, 'PostalZipCode', None)
            self.AccountProvider = to_enum(Provider, getattr(obj, 'AccountProvider', None))
            self.BoardingStatus = getattr(obj, 'BoardingStatus', None)

            self.BoardingFiles = []
            if hasattr(obj, 'BoardingFiles') and obj.BoardingFiles is not None:
                self.BoardingFiles = [BoardingFile(name) for name in  obj.BoardingFiles]


