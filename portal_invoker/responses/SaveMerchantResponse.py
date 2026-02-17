

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
            if not obj.HasError:
                self.TwoFactorStatus = TwoFactorStatus(getattr(obj, 'TwoFactorStatus', None)) if getattr(obj, 'TwoFactorStatus', None) is not None else None
                self.TwoFactorMessage = getattr(obj, 'TwoFactorMessage', None)
                self.TwoFactorSetupData = TwoFactorSetupData(getattr(obj, 'TwoFactorSetupData', None)) if getattr(obj, 'TwoFactorSetupData', None) is not None else None
                self.TwoFactorVerificationMerchantId = getattr(obj, 'TwoFactorVerificationMerchantId', None)
                self.TwoFactorVerificationMerchantName = getattr(obj, 'TwoFactorVerificationMerchantName', None)


