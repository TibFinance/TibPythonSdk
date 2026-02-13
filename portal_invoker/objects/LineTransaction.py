

from .BaseTransaction import BaseTransaction
from ..enums import AcpOperationType
from ..enums import LineType


class LineTransaction(BaseTransaction):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Amount = None
            self.DateFundsAvailable = None
            self.TargetInstitutionNumber = None
            self.TargetFullAccountNumber = None
            self.TargetName = None
            self.RefNumber = None
            self.OperationType = None
            self.LineType = None

        else:
            super().__init__(obj)

            self.Amount = getattr(obj, 'Amount', None)
            self.DateFundsAvailable = getattr(obj, 'DateFundsAvailable', None)
            self.TargetInstitutionNumber = getattr(obj, 'TargetInstitutionNumber', None)
            self.TargetFullAccountNumber = getattr(obj, 'TargetFullAccountNumber', None)
            self.TargetName = getattr(obj, 'TargetName', None)
            self.RefNumber = getattr(obj, 'RefNumber', None)
            self.OperationType = AcpOperationType(getattr(obj, 'OperationType', None)) if getattr(obj, 'OperationType', None) is not None else None
            self.LineType = LineType(getattr(obj, 'LineType', None)) if getattr(obj, 'LineType', None) is not None else None


