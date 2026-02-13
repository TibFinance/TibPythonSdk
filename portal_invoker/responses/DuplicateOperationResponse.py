

from .BaseApiResponse import BaseApiResponse
from ..objects import AdminOperation


class DuplicateOperationResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Operation = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Operation = AdminOperation(getattr(obj, 'Operation', None)) if getattr(obj, 'Operation', None) is not None else None


