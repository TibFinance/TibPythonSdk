
from ..utility import to_enum

from ..enums import Currency
from ..enums import Language
from ..enums import TransferFrequency


class CreateSupplierTransferArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.Amount = None
            self.TransferDueDate = None
            self.TargetMerchantId = None
            self.Currency = None
            self.Language = None
            self.TransferFrequency = None
            self.RecurringEndDate = None
            self.BillNumber = None
            self.BillDescription = None
            self.BillTitle = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.TransferDueDate = getattr(obj, 'TransferDueDate', None)
            self.TargetMerchantId = getattr(obj, 'TargetMerchantId', None)
            self.Currency = to_enum(Currency, getattr(obj, 'Currency', None))
            self.Language = to_enum(Language, getattr(obj, 'Language', None))
            self.TransferFrequency = to_enum(TransferFrequency, getattr(obj, 'TransferFrequency', None))
            self.RecurringEndDate = getattr(obj, 'RecurringEndDate', None)
            self.BillNumber = getattr(obj, 'BillNumber', None)
            self.BillDescription = getattr(obj, 'BillDescription', None)
            self.BillTitle = getattr(obj, 'BillTitle', None)


