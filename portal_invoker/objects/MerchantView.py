


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
            self.WhiteLabelingId = None
            self.BoardingStatus = None
            self.BoardingInformationId = None
            self.BoardingFiles = None

        else:
            
            from .BoardingFile import BoardingFile
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.AccountName = getattr(obj, 'AccountName', None)
            self.AccountPreview = getattr(obj, 'AccountPreview', None)
            self.ExternalSystemId = getattr(obj, 'ExternalSystemId', None)
            self.ExternalSystemGroupId = getattr(obj, 'ExternalSystemGroupId', None)
            self.MerchantCurrency = Currency(getattr(obj, 'MerchantCurrency', None)) if getattr(obj, 'MerchantCurrency', None) is not None else None
            self.MerchantLanguage = Language(getattr(obj, 'MerchantLanguage', None)) if getattr(obj, 'MerchantLanguage', None) is not None else None
            self.Email = getattr(obj, 'Email', None)
            self.IsAuthorized = getattr(obj, 'IsAuthorized', None)
            self.EmailCopyTo = getattr(obj, 'EmailCopyTo', None)
            self.MerchantPhoneNumber = getattr(obj, 'MerchantPhoneNumber', None)
            self.StreetAddress = getattr(obj, 'StreetAddress', None)
            self.AddressCity = getattr(obj, 'AddressCity', None)
            self.ProvinceStateId = ProvinceStateId(getattr(obj, 'ProvinceStateId', None)) if getattr(obj, 'ProvinceStateId', None) is not None else None
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.CountryId = CountryId(getattr(obj, 'CountryId', None)) if getattr(obj, 'CountryId', None) is not None else None
            self.PostalZipCode = getattr(obj, 'PostalZipCode', None)
            self.AccountProvider = Provider(getattr(obj, 'AccountProvider', None)) if getattr(obj, 'AccountProvider', None) is not None else None

            self.WhiteLabelingId = []
            if hasattr(obj, 'WhiteLabelingId') and obj.WhiteLabelingId is not None:
                self.WhiteLabelingId = [name for name in obj.WhiteLabelingId]
            self.BoardingStatus = getattr(obj, 'BoardingStatus', None)
            self.BoardingInformationId = getattr(obj, 'BoardingInformationId', None)

            self.BoardingFiles = []
            if hasattr(obj, 'BoardingFiles') and obj.BoardingFiles is not None:
                self.BoardingFiles = [BoardingFile(name) for name in  obj.BoardingFiles]


