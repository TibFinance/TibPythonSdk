

from .BaseApiResponse import BaseApiResponse


class CreateFreeOperationResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.PaymentId = None

        else:
            super().__init__(obj)
            self.PaymentId = getattr(obj, 'PaymentId', None)


