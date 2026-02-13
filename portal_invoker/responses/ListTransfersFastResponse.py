

from .BaseApiResponse import BaseApiResponse
from ..objects import TransferBaseInformationEntity


class ListTransfersFastResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Transfers = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.Transfers = []
                if hasattr(obj, 'Transfers') and obj.Transfers is not None:
                    self.Transfers = [TransferBaseInformationEntity(name) for name in  obj.Transfers]


