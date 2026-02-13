

from .BaseApiResponse import BaseApiResponse
from ..objects import FreeDepositOperation


class GetFreeDepositOperationsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.OperationList = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.OperationList = []
                if hasattr(obj, 'OperationList') and obj.OperationList is not None:
                    self.OperationList = [FreeDepositOperation(name) for name in  obj.OperationList]


