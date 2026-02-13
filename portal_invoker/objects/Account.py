


from ..enums import AccountType
from ..enums import Currency


class Account:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AccountName = None
            self.Owner = None
            self.FirstName = None
            self.LastName = None
            self.AccountType = None
            self.BankNumber = None
            self.InstitutionNumber = None
            self.AccountNumber = None
            self.RoutingNumber = None
            self.CheckDigit = None
            self.Currency = None
            self.FullAccountNumber = None
            self.AccountNumberWithCheckDigit = None
            self.PreviewString = None

        else:
            
            self.AccountName = getattr(obj, 'AccountName', None)
            self.Owner = getattr(obj, 'Owner', None)
            self.FirstName = getattr(obj, 'FirstName', None)
            self.LastName = getattr(obj, 'LastName', None)
            self.AccountType = AccountType(getattr(obj, 'AccountType', None)) if getattr(obj, 'AccountType', None) is not None else None
            self.BankNumber = getattr(obj, 'BankNumber', None)
            self.InstitutionNumber = getattr(obj, 'InstitutionNumber', None)
            self.AccountNumber = getattr(obj, 'AccountNumber', None)
            self.RoutingNumber = getattr(obj, 'RoutingNumber', None)
            self.CheckDigit = getattr(obj, 'CheckDigit', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.FullAccountNumber = getattr(obj, 'FullAccountNumber', None)
            self.AccountNumberWithCheckDigit = getattr(obj, 'AccountNumberWithCheckDigit', None)
            self.PreviewString = getattr(obj, 'PreviewString', None)


