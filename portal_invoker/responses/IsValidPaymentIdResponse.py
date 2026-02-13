

from .BaseApiResponse import BaseApiResponse


class IsValidPaymentIdResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.IsValidPaymentId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.IsValidPaymentId = getattr(obj, 'IsValidPaymentId', None)


