

from .BaseApiResponse import BaseApiResponse
from ..objects import MontlyBillInfo


class GetAllClientsBillResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BillsInfo = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.BillsInfo = []
                if hasattr(obj, 'BillsInfo') and obj.BillsInfo is not None:
                    self.BillsInfo = [MontlyBillInfo(name) for name in  obj.BillsInfo]


