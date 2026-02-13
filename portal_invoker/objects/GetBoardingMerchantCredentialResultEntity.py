

from .BoardingBaseResult import BoardingBaseResult


class GetBoardingMerchantCredentialResultEntity(BoardingBaseResult):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.MerchantId = None
            self.UserName = None
            self.Password = None
            self.DataProtectionKey = None

        else:
            super().__init__(obj)

            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.UserName = getattr(obj, 'UserName', None)
            self.Password = getattr(obj, 'Password', None)
            self.DataProtectionKey = getattr(obj, 'DataProtectionKey', None)


