

from .BaseApiResponse import BaseApiResponse
from ..objects import BinInfoDto


class GetBinInfoResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BinInfo = None
            self.Found = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.BinInfo = BinInfoDto(getattr(obj, 'BinInfo', None)) if getattr(obj, 'BinInfo', None) is not None else None
                self.Found = getattr(obj, 'Found', None)


