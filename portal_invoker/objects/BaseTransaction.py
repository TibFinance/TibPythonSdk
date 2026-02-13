

from .LineBase import LineBase
from ..enums import AcpOperationType
from ..enums import TransferFrequency


class BaseTransaction(LineBase):
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
            self.TargetContactInfo = None
            self.TransferFrequency = None

        else:
            super().__init__(obj)

            from .ContactInfo import ContactInfo
            self.Amount = getattr(obj, 'Amount', None)
            self.DateFundsAvailable = getattr(obj, 'DateFundsAvailable', None)
            self.TargetInstitutionNumber = getattr(obj, 'TargetInstitutionNumber', None)
            self.TargetFullAccountNumber = getattr(obj, 'TargetFullAccountNumber', None)
            self.TargetName = getattr(obj, 'TargetName', None)
            self.RefNumber = getattr(obj, 'RefNumber', None)
            self.OperationType = AcpOperationType(getattr(obj, 'OperationType', None)) if getattr(obj, 'OperationType', None) is not None else None
            self.TargetContactInfo = ContactInfo(getattr(obj, 'TargetContactInfo', None)) if getattr(obj, 'TargetContactInfo', None) is not None else None
            self.TransferFrequency = TransferFrequency(getattr(obj, 'TransferFrequency', None)) if getattr(obj, 'TransferFrequency', None) is not None else None


