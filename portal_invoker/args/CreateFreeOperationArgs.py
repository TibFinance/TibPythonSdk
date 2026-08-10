
from ..utility import to_enum

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
            self.RecurringEndDate = None
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
            self.TransferType = to_enum(TransferType, getattr(obj, 'TransferType', None))
            self.ReferenceNumber = getattr(obj, 'ReferenceNumber', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.Language = to_enum(Language, getattr(obj, 'Language', None))
            self.TransactionDueDate = getattr(obj, 'TransactionDueDate', None)
            self.TransferTitle = getattr(obj, 'TransferTitle', None)
            self.TransferDescription = getattr(obj, 'TransferDescription', None)
            self.TransferExternalSystemNumber = getattr(obj, 'TransferExternalSystemNumber', None)
            self.TransferFrequency = to_enum(TransferFrequency, getattr(obj, 'TransferFrequency', None))
            self.RecurringEndDate = getattr(obj, 'RecurringEndDate', None)
            self.GroupId = getattr(obj, 'GroupId', None)
            self.ImmediateTransfer = getattr(obj, 'ImmediateTransfer', None)
            self.StatementDescription = getattr(obj, 'StatementDescription', None)
            self.StopSameIdentifications = getattr(obj, 'StopSameIdentifications', None)


