

from .BaseApiResponse import BaseApiResponse
from ..objects import Bill


class ListBillsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Bills = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.Bills = []
                if hasattr(obj, 'Bills') and obj.Bills is not None:
                    self.Bills = [Bill(name) for name in  obj.Bills]


