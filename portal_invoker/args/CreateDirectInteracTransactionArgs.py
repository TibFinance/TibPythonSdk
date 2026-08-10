
from ..utility import to_enum

from ..objects import Interac
from ..enums import TransferDirection
from ..enums import Currency
from ..enums import Language


class CreateDirectInteracTransactionArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.InteracInformation = None
            self.TransferDirection = None
            self.DueDate = None
            self.Amount = None
            self.StatementDescription = None
            self.Currency = None
            self.Language = None
            self.ReferenceNumber = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.InteracInformation = Interac(getattr(obj, 'InteracInformation', None)) if getattr(obj, 'InteracInformation', None) is not None else None
            self.TransferDirection = to_enum(TransferDirection, getattr(obj, 'TransferDirection', None))
            self.DueDate = getattr(obj, 'DueDate', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.StatementDescription = getattr(obj, 'StatementDescription', None)
            self.Currency = to_enum(Currency, getattr(obj, 'Currency', None))
            self.Language = to_enum(Language, getattr(obj, 'Language', None))
            self.ReferenceNumber = getattr(obj, 'ReferenceNumber', None)


