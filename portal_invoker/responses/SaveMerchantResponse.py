
from ..utility import to_enum
from .BaseApiResponse import BaseApiResponse
from ..enums import TwoFactorStatus
from ..objects import TwoFactorSetupData


class SaveMerchantResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.TwoFactorStatus = None
            self.TwoFactorMessage = None
            self.TwoFactorSetupData = None
            self.TwoFactorVerificationMerchantId = None
            self.TwoFactorVerificationMerchantName = None

        else:
            super().__init__(obj)
            self.TwoFactorStatus = to_enum(TwoFactorStatus, getattr(obj, 'TwoFactorStatus', None))
            self.TwoFactorMessage = getattr(obj, 'TwoFactorMessage', None)
            self.TwoFactorSetupData = TwoFactorSetupData(getattr(obj, 'TwoFactorSetupData', None)) if getattr(obj, 'TwoFactorSetupData', None) is not None else None
            self.TwoFactorVerificationMerchantId = getattr(obj, 'TwoFactorVerificationMerchantId', None)
            self.TwoFactorVerificationMerchantName = getattr(obj, 'TwoFactorVerificationMerchantName', None)


