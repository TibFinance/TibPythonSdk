

from .BaseApiResponse import BaseApiResponse
from ..responses import RequestDataResponse


class CreateFreeOperationBatchResponseBase(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Status = None
            self.PaymentId = None
            self.ReferenceNumber = None
            self.Message = None
            self.RequestDataResponse = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Status = getattr(obj, 'Status', None)
                self.PaymentId = getattr(obj, 'PaymentId', None)
                self.ReferenceNumber = getattr(obj, 'ReferenceNumber', None)
                self.Message = getattr(obj, 'Message', None)
                self.RequestDataResponse = RequestDataResponse(getattr(obj, 'RequestDataResponse', None)) if getattr(obj, 'RequestDataResponse', None) is not None else None


