

from .BaseApiResponse import BaseApiResponse
from ..objects import PendingTransferDto


class GetPendingTransferApprovalsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.PendingTransfers = None

        else:
            super().__init__(obj)

            self.PendingTransfers = []
            if hasattr(obj, 'PendingTransfers') and obj.PendingTransfers is not None:
                self.PendingTransfers = [PendingTransferDto(name) for name in  obj.PendingTransfers]


