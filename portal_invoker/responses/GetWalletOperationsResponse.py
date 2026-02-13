

from .BaseApiResponse import BaseApiResponse
from ..objects import WalletOperation


class GetWalletOperationsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.DailyOperations = None
            self.BalanceBeforeOperations = None
            self.DelayBufferAmount = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.DailyOperations = []
                if hasattr(obj, 'DailyOperations') and obj.DailyOperations is not None:
                    self.DailyOperations = [WalletOperation(name) for name in  obj.DailyOperations]
                self.BalanceBeforeOperations = getattr(obj, 'BalanceBeforeOperations', None)
                self.DelayBufferAmount = getattr(obj, 'DelayBufferAmount', None)


