

from .BaseApiResponse import BaseApiResponse


class GetBoardingApprovalResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ApprovalStatus = None
            self.MerchantName = None
            self.MerchantEmail = None
            self.MerchantId = None
            self.SandboxId = None
            self.Processing = None
            self.Payout = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.ApprovalStatus = getattr(obj, 'ApprovalStatus', None)
                self.MerchantName = getattr(obj, 'MerchantName', None)
                self.MerchantEmail = getattr(obj, 'MerchantEmail', None)
                self.MerchantId = getattr(obj, 'MerchantId', None)
                self.SandboxId = getattr(obj, 'SandboxId', None)
                self.Processing = getattr(obj, 'Processing', None)
                self.Payout = getattr(obj, 'Payout', None)


