

from .BaseApiResponse import BaseApiResponse
from ..objects import BoardingResultEntity


class BoardingResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BoardingResultEntity = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.BoardingResultEntity = BoardingResultEntity(getattr(obj, 'BoardingResultEntity', None)) if getattr(obj, 'BoardingResultEntity', None) is not None else None


