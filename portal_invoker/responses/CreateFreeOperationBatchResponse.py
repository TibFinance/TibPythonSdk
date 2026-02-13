

from .BaseApiResponse import BaseApiResponse
from ..responses import CreateFreeOperationBatchResponseBase


class CreateFreeOperationBatchResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CreateFreeOperationBatchResponses = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.CreateFreeOperationBatchResponses = []
                if hasattr(obj, 'CreateFreeOperationBatchResponses') and obj.CreateFreeOperationBatchResponses is not None:
                    self.CreateFreeOperationBatchResponses = [CreateFreeOperationBatchResponseBase(name) for name in  obj.CreateFreeOperationBatchResponses]


