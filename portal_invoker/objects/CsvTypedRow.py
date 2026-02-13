


from ..enums import TransferDirection
from ..enums import ProvinceStateId
from ..enums import CountryId
from ..enums import Language
from ..enums import TransferFrequency


class CsvTypedRow:
    def __init__(self, obj=None):
        if obj is None:
            
            self.OrganizationNumber = None
            self.FileNumber = None
            self.OperationType = None
            self.Amount = None
            self.DateFundsAvailable = None
            self.TargetName = None
            self.TargetInstitutionNumber = None
            self.TargetFullAccountNumber = None
            self.RefNumber = None
            self.Email = None
            self.Phone = None
            self.Address = None
            self.City = None
            self.Province = None
            self.Country = None
            self.ZipCode = None
            self.Language = None
            self.Frequency = None

        else:
            
            self.OrganizationNumber = getattr(obj, 'OrganizationNumber', None)
            self.FileNumber = getattr(obj, 'FileNumber', None)
            self.OperationType = TransferDirection(getattr(obj, 'OperationType', None)) if getattr(obj, 'OperationType', None) is not None else None
            self.Amount = getattr(obj, 'Amount', None)
            self.DateFundsAvailable = getattr(obj, 'DateFundsAvailable', None)
            self.TargetName = getattr(obj, 'TargetName', None)
            self.TargetInstitutionNumber = getattr(obj, 'TargetInstitutionNumber', None)
            self.TargetFullAccountNumber = getattr(obj, 'TargetFullAccountNumber', None)
            self.RefNumber = getattr(obj, 'RefNumber', None)
            self.Email = getattr(obj, 'Email', None)
            self.Phone = getattr(obj, 'Phone', None)
            self.Address = getattr(obj, 'Address', None)
            self.City = getattr(obj, 'City', None)
            self.Province = ProvinceStateId(getattr(obj, 'Province', None)) if getattr(obj, 'Province', None) is not None else None
            self.Country = CountryId(getattr(obj, 'Country', None)) if getattr(obj, 'Country', None) is not None else None
            self.ZipCode = getattr(obj, 'ZipCode', None)
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.Frequency = TransferFrequency(getattr(obj, 'Frequency', None)) if getattr(obj, 'Frequency', None) is not None else None


