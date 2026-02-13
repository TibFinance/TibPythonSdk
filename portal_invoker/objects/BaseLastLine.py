

from .LineBaseWithHeader import LineBaseWithHeader


class BaseLastLine(LineBaseWithHeader):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.TotalAmountCollected = None
            self.NumberOfTransactionCollected = None
            self.TotalAmountDeposit = None
            self.NumberOfTransactionDeposit = None

        else:
            super().__init__(obj)

            self.TotalAmountCollected = getattr(obj, 'TotalAmountCollected', None)
            self.NumberOfTransactionCollected = getattr(obj, 'NumberOfTransactionCollected', None)
            self.TotalAmountDeposit = getattr(obj, 'TotalAmountDeposit', None)
            self.NumberOfTransactionDeposit = getattr(obj, 'NumberOfTransactionDeposit', None)


