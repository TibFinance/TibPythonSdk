

from .TransactionCommon import TransactionCommon


class TransactionCommonWithMeta(TransactionCommon):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.TransactionId = None
            self.TransactionAmount = None

        else:
            super().__init__(obj)

            self.TransactionId = getattr(obj, 'TransactionId', None)
            self.TransactionAmount = getattr(obj, 'TransactionAmount', None)


