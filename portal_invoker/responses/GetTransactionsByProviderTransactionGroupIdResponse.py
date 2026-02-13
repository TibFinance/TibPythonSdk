

from .BaseApiResponse import BaseApiResponse
from ..objects import TransactionCommonWithMeta


class GetTransactionsByProviderTransactionGroupIdResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Transactions = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.Transactions = []
                if hasattr(obj, 'Transactions') and obj.Transactions is not None:
                    self.Transactions = [TransactionCommonWithMeta(name) for name in  obj.Transactions]


