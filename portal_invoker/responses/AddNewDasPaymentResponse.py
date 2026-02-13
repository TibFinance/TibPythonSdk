

from .BaseApiResponse import BaseApiResponse


class AddNewDasPaymentResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.DasPaymentId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.DasPaymentId = getattr(obj, 'DasPaymentId', None)


