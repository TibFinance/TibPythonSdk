

from .BaseApiResponse import BaseApiResponse
from ..objects import WhiteLabeling


class GetWhiteLabelingResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.WhiteLabeling = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.WhiteLabeling = WhiteLabeling(getattr(obj, 'WhiteLabeling', None)) if getattr(obj, 'WhiteLabeling', None) is not None else None


