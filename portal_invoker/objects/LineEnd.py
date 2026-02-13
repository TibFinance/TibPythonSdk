

from .BaseLastLine import BaseLastLine


class LineEnd(BaseLastLine):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.TotalAmountCollected = None
            self.NumberOfTransactionCollected = None
            self.TotalAmountDeposit = None
            self.NumberOfTransactionDeposit = None
            self.StartPosition = None

        else:
            super().__init__(obj)

            self.TotalAmountCollected = getattr(obj, 'TotalAmountCollected', None)
            self.NumberOfTransactionCollected = getattr(obj, 'NumberOfTransactionCollected', None)
            self.TotalAmountDeposit = getattr(obj, 'TotalAmountDeposit', None)
            self.NumberOfTransactionDeposit = getattr(obj, 'NumberOfTransactionDeposit', None)
            self.StartPosition = getattr(obj, 'StartPosition', None)


