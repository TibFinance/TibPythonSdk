
from ..utility import to_enum

from ..enums import Currency


class Account:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AccountName = None
            self.Owner = None
            self.BankNumber = None
            self.InstitutionNumber = None
            self.AccountNumber = None
            self.RoutingNumber = None
            self.CheckDigit = None
            self.Currency = None

        else:
            
            self.AccountName = getattr(obj, 'AccountName', None)
            self.Owner = getattr(obj, 'Owner', None)
            self.BankNumber = getattr(obj, 'BankNumber', None)
            self.InstitutionNumber = getattr(obj, 'InstitutionNumber', None)
            self.AccountNumber = getattr(obj, 'AccountNumber', None)
            self.RoutingNumber = getattr(obj, 'RoutingNumber', None)
            self.CheckDigit = getattr(obj, 'CheckDigit', None)
            self.Currency = to_enum(Currency, getattr(obj, 'Currency', None))


