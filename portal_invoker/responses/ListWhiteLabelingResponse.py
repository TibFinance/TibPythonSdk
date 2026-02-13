

from .BaseApiResponse import BaseApiResponse
from ..objects import WhiteLabeling


class ListWhiteLabelingResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.whiteLabelings = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.whiteLabelings = []
                if hasattr(obj, 'whiteLabelings') and obj.whiteLabelings is not None:
                    self.whiteLabelings = [WhiteLabeling(name) for name in  obj.whiteLabelings]


