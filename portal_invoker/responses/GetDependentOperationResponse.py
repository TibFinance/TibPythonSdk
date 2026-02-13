

from .BaseApiResponse import BaseApiResponse
from ..objects import DependentOperation


class GetDependentOperationResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.OperationIds = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.OperationIds = []
                if hasattr(obj, 'OperationIds') and obj.OperationIds is not None:
                    self.OperationIds = [DependentOperation(name) for name in  obj.OperationIds]


