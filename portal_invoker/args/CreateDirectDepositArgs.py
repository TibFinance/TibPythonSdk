


from ..objects import Account
from ..enums import Currency
from ..enums import Language


class CreateDirectDepositArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.OriginMerchantId = None
            self.DestinationAccount = None
            self.DepositDueDate = None
            self.Amount = None
            self.StatementDescription = None
            self.Currency = None
            self.Language = None
            self.ReferenceNumber = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.OriginMerchantId = getattr(obj, 'OriginMerchantId', None)
            self.DestinationAccount = Account(getattr(obj, 'DestinationAccount', None)) if getattr(obj, 'DestinationAccount', None) is not None else None
            self.DepositDueDate = getattr(obj, 'DepositDueDate', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.StatementDescription = getattr(obj, 'StatementDescription', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.ReferenceNumber = getattr(obj, 'ReferenceNumber', None)


