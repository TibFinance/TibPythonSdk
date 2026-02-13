


from ..enums import TransferType
from ..enums import Language
from ..enums import TransferFrequency


class CreateFreeOperationArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.BillId = None
            self.CustomerId = None
            self.PaymentMethodId = None
            self.TransferType = None
            self.ReferenceNumber = None
            self.Amount = None
            self.Language = None
            self.TransactionDueDate = None
            self.TransferTitle = None
            self.TransferDescription = None
            self.TransferExternalSystemNumber = None
            self.TransferFrequency = None
            self.GroupId = None
            self.ImmediateTransfer = None
            self.StatementDescription = None
            self.StopSameIdentifications = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.BillId = getattr(obj, 'BillId', None)
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.PaymentMethodId = getattr(obj, 'PaymentMethodId', None)
            self.TransferType = TransferType(getattr(obj, 'TransferType', None)) if getattr(obj, 'TransferType', None) is not None else None
            self.ReferenceNumber = getattr(obj, 'ReferenceNumber', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.TransactionDueDate = getattr(obj, 'TransactionDueDate', None)
            self.TransferTitle = getattr(obj, 'TransferTitle', None)
            self.TransferDescription = getattr(obj, 'TransferDescription', None)
            self.TransferExternalSystemNumber = getattr(obj, 'TransferExternalSystemNumber', None)
            self.TransferFrequency = TransferFrequency(getattr(obj, 'TransferFrequency', None)) if getattr(obj, 'TransferFrequency', None) is not None else None
            self.GroupId = getattr(obj, 'GroupId', None)
            self.ImmediateTransfer = getattr(obj, 'ImmediateTransfer', None)
            self.StatementDescription = getattr(obj, 'StatementDescription', None)
            self.StopSameIdentifications = getattr(obj, 'StopSameIdentifications', None)


