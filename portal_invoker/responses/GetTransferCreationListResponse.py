

from .BaseApiResponse import BaseApiResponse
from ..objects import TransferCreation


class GetTransferCreationListResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.TransfersCreations = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.TransfersCreations = []
                if hasattr(obj, 'TransfersCreations') and obj.TransfersCreations is not None:
                    self.TransfersCreations = [TransferCreation(name) for name in  obj.TransfersCreations]


