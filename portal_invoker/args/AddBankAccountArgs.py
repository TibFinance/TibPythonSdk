


from ..enums import Language


class AddBankAccountArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ServiceId = None
            self.Name = None
            self.Email = None
            self.Language = None
            self.BankNumber = None
            self.InstitutionNumber = None
            self.AccountNumber = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.Name = getattr(obj, 'Name', None)
            self.Email = getattr(obj, 'Email', None)
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.BankNumber = getattr(obj, 'BankNumber', None)
            self.InstitutionNumber = getattr(obj, 'InstitutionNumber', None)
            self.AccountNumber = getattr(obj, 'AccountNumber', None)


