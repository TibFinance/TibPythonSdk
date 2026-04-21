

from .BaseApiResponse import BaseApiResponse
from ..objects import RecuringTransfer


class ListSupplierRecurringTransfersResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.RecurringTransfers = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.RecurringTransfers = []
                if hasattr(obj, 'RecurringTransfers') and obj.RecurringTransfers is not None:
                    self.RecurringTransfers = [RecuringTransfer(name) for name in  obj.RecurringTransfers]


