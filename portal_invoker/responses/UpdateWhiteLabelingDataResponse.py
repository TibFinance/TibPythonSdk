

from .BaseApiResponse import BaseApiResponse
from ..objects import WhiteLabeling


class UpdateWhiteLabelingDataResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.WhiteLabeling = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.WhiteLabeling = WhiteLabeling(obj.WhiteLabeling)


