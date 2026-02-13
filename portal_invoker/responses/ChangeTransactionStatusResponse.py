

from .BaseApiResponse import BaseApiResponse


class ChangeTransactionStatusResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.TransactionId = None
            self.TransactionStatus = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.TransactionId = getattr(obj, 'TransactionId', None)
                self.TransactionStatus = getattr(obj, 'TransactionStatus', None)


