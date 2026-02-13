

from .BaseApiResponse import BaseApiResponse


class CreateBillResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BillId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.BillId = getattr(obj, 'BillId', None)


