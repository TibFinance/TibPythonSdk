

from .BaseApiResponse import BaseApiResponse
from ..enums import BoardingStatus


class ProcessWebHookResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BoardingInformationId = None
            self.TransactionType = None
            self.BoardingStatus = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.BoardingInformationId = getattr(obj, 'BoardingInformationId', None)
                self.TransactionType = getattr(obj, 'TransactionType', None)
                self.BoardingStatus = BoardingStatus(getattr(obj, 'BoardingStatus', None)) if getattr(obj, 'BoardingStatus', None) is not None else None


