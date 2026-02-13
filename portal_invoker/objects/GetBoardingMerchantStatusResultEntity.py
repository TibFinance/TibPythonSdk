

from .BoardingBaseResult import BoardingBaseResult


class GetBoardingMerchantStatusResultEntity(BoardingBaseResult):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.MerchantName = None
            self.MerchantEmail = None
            self.ProviderMerchantId = None
            self.MerchantId = None
            self.SandboxId = None
            self.Processing = None
            self.Payout = None

        else:
            super().__init__(obj)

            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.MerchantEmail = getattr(obj, 'MerchantEmail', None)
            self.ProviderMerchantId = getattr(obj, 'ProviderMerchantId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.SandboxId = getattr(obj, 'SandboxId', None)
            self.Processing = getattr(obj, 'Processing', None)
            self.Payout = getattr(obj, 'Payout', None)


