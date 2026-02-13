

from .BaseApiResponse import BaseApiResponse
from ..objects import WhiteLabeling


class GetChangeValidationResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.JsonObject = None
            self.ValidationToken = None
            self.WhiteLabeling = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.JsonObject = getattr(obj, 'JsonObject', None)
                self.ValidationToken = getattr(obj, 'ValidationToken', None)
                self.WhiteLabeling = WhiteLabeling(getattr(obj, 'WhiteLabeling', None)) if getattr(obj, 'WhiteLabeling', None) is not None else None


