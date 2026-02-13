

from .BaseApiResponse import BaseApiResponse


class CreateFreeOperationResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.PaymentId = None
            self.ClientId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.PaymentId = getattr(obj, 'PaymentId', None)
                self.ClientId = getattr(obj, 'ClientId', None)


