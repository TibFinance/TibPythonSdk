
from ..utility import to_enum

from ..enums import OperationTarget
from ..enums import OperationType
from ..enums import TransferDirection
from ..enums import OperationStatus
from ..enums import BankingOperationResult
from ..enums import PaymentMethodType


class TransactionCommon:
    def __init__(self, obj=None):
        if obj is None:
            
            self.OperationTarget = None
            self.OperationType = None
            self.OperationDirection = None
            self.Status = None
            self.Description = None
            self.BankingOperationResult = None
            self.BankDescription = None
            self.AccountName = None
            self.AccoutPreview = None
            self.AccountType = None
            self.TransactionDescription = None
            self.TransactionDueDate = None
            self.LastModifiedDate = None

        else:
            
            self.OperationTarget = to_enum(OperationTarget, getattr(obj, 'OperationTarget', None))
            self.OperationType = to_enum(OperationType, getattr(obj, 'OperationType', None))
            self.OperationDirection = to_enum(TransferDirection, getattr(obj, 'OperationDirection', None))
            self.Status = to_enum(OperationStatus, getattr(obj, 'Status', None))
            self.Description = getattr(obj, 'Description', None)
            self.BankingOperationResult = to_enum(BankingOperationResult, getattr(obj, 'BankingOperationResult', None))
            self.BankDescription = getattr(obj, 'BankDescription', None)
            self.AccountName = getattr(obj, 'AccountName', None)
            self.AccoutPreview = getattr(obj, 'AccoutPreview', None)
            self.AccountType = to_enum(PaymentMethodType, getattr(obj, 'AccountType', None))
            self.TransactionDescription = getattr(obj, 'TransactionDescription', None)
            self.TransactionDueDate = getattr(obj, 'TransactionDueDate', None)
            self.LastModifiedDate = getattr(obj, 'LastModifiedDate', None)


