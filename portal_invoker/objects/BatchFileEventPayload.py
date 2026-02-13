

from .BaseEventPayload import BaseEventPayload


class BatchFileEventPayload(BaseEventPayload):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.File = None
            self.Operations = None

        else:
            super().__init__(obj)

            from .BatchFileEventOperation import BatchFileEventOperation
            self.File = getattr(obj, 'File', None)

            self.Operations = []
            if hasattr(obj, 'Operations') and obj.Operations is not None:
                self.Operations = [BatchFileEventOperation(name) for name in  obj.Operations]


