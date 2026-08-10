

from .BaseApiResponse import BaseApiResponse
from ..objects import WalletOperation
from ..objects import WalletOperationDetail


class GetWalletOperationsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.DailyOperations = None
            self.BalanceBeforeOperations = None
            self.DelayBufferAmount = None
            self.OperationDetails = None

        else:
            super().__init__(obj)

            self.DailyOperations = []
            if hasattr(obj, 'DailyOperations') and obj.DailyOperations is not None:
                self.DailyOperations = [WalletOperation(name) for name in  obj.DailyOperations]
            self.BalanceBeforeOperations = getattr(obj, 'BalanceBeforeOperations', None)
            self.DelayBufferAmount = getattr(obj, 'DelayBufferAmount', None)

            self.OperationDetails = []
            if hasattr(obj, 'OperationDetails') and obj.OperationDetails is not None:
                self.OperationDetails = [WalletOperationDetail(name) for name in  obj.OperationDetails]


