

from .BaseApiResponse import BaseApiResponse


class CreateTransactionFromRawResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.TransactionsGroupId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.TransactionsGroupId = getattr(obj, 'TransactionsGroupId', None)


