
from ..utility import to_enum

from ..enums import Currency
from ..enums import Language


class CreateSupplierArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.SupplierName = None
            self.SupplierEmail = None
            self.Currency = None
            self.Language = None
            self.AccountNumber = None
            self.BankNumber = None
            self.InstitutionNumber = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.SupplierName = getattr(obj, 'SupplierName', None)
            self.SupplierEmail = getattr(obj, 'SupplierEmail', None)
            self.Currency = to_enum(Currency, getattr(obj, 'Currency', None))
            self.Language = to_enum(Language, getattr(obj, 'Language', None))
            self.AccountNumber = getattr(obj, 'AccountNumber', None)
            self.BankNumber = getattr(obj, 'BankNumber', None)
            self.InstitutionNumber = getattr(obj, 'InstitutionNumber', None)


