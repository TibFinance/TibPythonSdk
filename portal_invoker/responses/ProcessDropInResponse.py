

from .BaseApiResponse import BaseApiResponse


class ProcessDropInResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.PaymentId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.PaymentId = getattr(obj, 'PaymentId', None)


