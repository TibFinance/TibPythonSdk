

from .BaseApiResponse import BaseApiResponse


class ChangeOperationStatusResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.OperationId = None
            self.OperationStatus = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.OperationId = getattr(obj, 'OperationId', None)
                self.OperationStatus = getattr(obj, 'OperationStatus', None)


