


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
            self.BillNumber = None
            self.BillDescription = None
            self.BillTitle = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.TransferDueDate = getattr(obj, 'TransferDueDate', None)
            self.TargetMerchantId = getattr(obj, 'TargetMerchantId', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.TransferFrequency = TransferFrequency(getattr(obj, 'TransferFrequency', None)) if getattr(obj, 'TransferFrequency', None) is not None else None
            self.BillNumber = getattr(obj, 'BillNumber', None)
            self.BillDescription = getattr(obj, 'BillDescription', None)
            self.BillTitle = getattr(obj, 'BillTitle', None)


