

from .BaseApiResponse import BaseApiResponse
from ..objects import RecuringTransfer


class GetRecuringTransfersResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.RecuringTransfers = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.RecuringTransfers = []
                if hasattr(obj, 'RecuringTransfers') and obj.RecuringTransfers is not None:
                    self.RecuringTransfers = [RecuringTransfer(name) for name in  obj.RecuringTransfers]


