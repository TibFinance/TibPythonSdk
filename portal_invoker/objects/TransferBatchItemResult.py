
from ..utility import to_enum

from ..enums import TransferBatchItemOutcome
from ..enums import TransferBatchCustomerAction


class TransferBatchItemResult:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Index = None
            self.ReferenceNumber = None
            self.Outcome = None
            self.PaymentId = None
            self.CustomerId = None
            self.CustomerAction = None
            self.BankAccountKnown = None
            self.ErrorCode = None
            self.Message = None
            self.WarningCodes = None

        else:
            
            self.Index = getattr(obj, 'Index', None)
            self.ReferenceNumber = getattr(obj, 'ReferenceNumber', None)
            self.Outcome = to_enum(TransferBatchItemOutcome, getattr(obj, 'Outcome', None))
            self.PaymentId = getattr(obj, 'PaymentId', None)
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.CustomerAction = to_enum(TransferBatchCustomerAction, getattr(obj, 'CustomerAction', None))
            self.BankAccountKnown = getattr(obj, 'BankAccountKnown', None)
            self.ErrorCode = getattr(obj, 'ErrorCode', None)
            self.Message = getattr(obj, 'Message', None)

            self.WarningCodes = []
            if hasattr(obj, 'WarningCodes') and obj.WarningCodes is not None:
                self.WarningCodes = [name for name in obj.WarningCodes]


