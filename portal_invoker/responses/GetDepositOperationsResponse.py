

from .BaseApiResponse import BaseApiResponse
from ..objects import Operation


class GetDepositOperationsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.OperationList = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.OperationList = []
                if hasattr(obj, 'OperationList') and obj.OperationList is not None:
                    self.OperationList = [Operation(name) for name in  obj.OperationList]


