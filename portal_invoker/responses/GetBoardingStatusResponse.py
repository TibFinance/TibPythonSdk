

from .BaseApiResponse import BaseApiResponse


class GetBoardingStatusResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.MerchantId = None
            self.MerchantName = None
            self.Currency = None
            self.MerchantLanguage = None
            self.MerchantEmail = None
            self.AuthorizationStatus = None
            self.CreatedDate = None
            self.PhoneNumber = None
            self.MerchantDescription = None
            self.AccountName = None
            self.AccountInformation = None
            self.BoardingStatus = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.MerchantId = getattr(obj, 'MerchantId', None)
                self.MerchantName = getattr(obj, 'MerchantName', None)
                self.Currency = getattr(obj, 'Currency', None)
                self.MerchantLanguage = getattr(obj, 'MerchantLanguage', None)
                self.MerchantEmail = getattr(obj, 'MerchantEmail', None)
                self.AuthorizationStatus = getattr(obj, 'AuthorizationStatus', None)
                self.CreatedDate = getattr(obj, 'CreatedDate', None)
                self.PhoneNumber = getattr(obj, 'PhoneNumber', None)
                self.MerchantDescription = getattr(obj, 'MerchantDescription', None)
                self.AccountName = getattr(obj, 'AccountName', None)
                self.AccountInformation = getattr(obj, 'AccountInformation', None)
                self.BoardingStatus = getattr(obj, 'BoardingStatus', None)


