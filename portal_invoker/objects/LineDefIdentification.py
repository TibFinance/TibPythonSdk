

from .LineBaseWithHeader import LineBaseWithHeader
from ..enums import Currency


class LineDefIdentification(LineBaseWithHeader):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CreationDate = None
            self.BankCentral = None
            self.MoneyCodeIdentifier = None

        else:
            super().__init__(obj)

            self.CreationDate = getattr(obj, 'CreationDate', None)
            self.BankCentral = getattr(obj, 'BankCentral', None)
            self.MoneyCodeIdentifier = Currency(getattr(obj, 'MoneyCodeIdentifier', None)) if getattr(obj, 'MoneyCodeIdentifier', None) is not None else None


