

from .BaseApiResponse import BaseApiResponse
from ..objects import DropInEntity
from ..objects import WhiteLabeling


class GetDropInResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.DropIn = None
            self.WhiteLabeling = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.DropIn = DropInEntity(getattr(obj, 'DropIn', None)) if getattr(obj, 'DropIn', None) is not None else None
                self.WhiteLabeling = WhiteLabeling(getattr(obj, 'WhiteLabeling', None)) if getattr(obj, 'WhiteLabeling', None) is not None else None


