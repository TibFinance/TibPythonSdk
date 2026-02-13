

from .BaseApiResponse import BaseApiResponse
from ..objects import Bill


class GetBillResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Bill = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Bill = Bill(getattr(obj, 'Bill', None)) if getattr(obj, 'Bill', None) is not None else None


