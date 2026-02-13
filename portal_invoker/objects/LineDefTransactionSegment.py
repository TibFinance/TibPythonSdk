

from .BaseTransaction import BaseTransaction
from ..enums import AcpOperationType


class LineDefTransactionSegment(BaseTransaction):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.StartPosition = None
            self.OperationType = None
            self.Amount = None
            self.DateFundsAvailable = None
            self.TargetInstitutionNumber = None
            self.TargetFullAccountNumber = None
            self.ShortOrganizationName = None
            self.TargetName = None
            self.OrganizationName = None
            self.OrganizationNumber = None
            self.RefNumber = None
            self.ReturnInstitution = None
            self.ReturnAccount = None
            self.FreeOrganizationField = None

        else:
            super().__init__(obj)

            self.StartPosition = getattr(obj, 'StartPosition', None)
            self.OperationType = AcpOperationType(getattr(obj, 'OperationType', None)) if getattr(obj, 'OperationType', None) is not None else None
            self.Amount = getattr(obj, 'Amount', None)
            self.DateFundsAvailable = getattr(obj, 'DateFundsAvailable', None)
            self.TargetInstitutionNumber = getattr(obj, 'TargetInstitutionNumber', None)
            self.TargetFullAccountNumber = getattr(obj, 'TargetFullAccountNumber', None)
            self.ShortOrganizationName = getattr(obj, 'ShortOrganizationName', None)
            self.TargetName = getattr(obj, 'TargetName', None)
            self.OrganizationName = getattr(obj, 'OrganizationName', None)
            self.OrganizationNumber = getattr(obj, 'OrganizationNumber', None)
            self.RefNumber = getattr(obj, 'RefNumber', None)
            self.ReturnInstitution = getattr(obj, 'ReturnInstitution', None)
            self.ReturnAccount = getattr(obj, 'ReturnAccount', None)
            self.FreeOrganizationField = getattr(obj, 'FreeOrganizationField', None)


