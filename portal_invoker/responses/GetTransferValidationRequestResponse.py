

from .BaseApiResponse import BaseApiResponse
from ..objects import TransferValidationEntity
from ..objects import WhiteLabeling


class GetTransferValidationRequestResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Transfer = None
            self.WhiteLabeling = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Transfer = TransferValidationEntity(getattr(obj, 'Transfer', None)) if getattr(obj, 'Transfer', None) is not None else None
                self.WhiteLabeling = WhiteLabeling(getattr(obj, 'WhiteLabeling', None)) if getattr(obj, 'WhiteLabeling', None) is not None else None


