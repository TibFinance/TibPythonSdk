


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
            
            self.OperationTarget = OperationTarget(getattr(obj, 'OperationTarget', None)) if getattr(obj, 'OperationTarget', None) is not None else None
            self.OperationType = OperationType(getattr(obj, 'OperationType', None)) if getattr(obj, 'OperationType', None) is not None else None
            self.OperationDirection = TransferDirection(getattr(obj, 'OperationDirection', None)) if getattr(obj, 'OperationDirection', None) is not None else None
            self.Status = OperationStatus(getattr(obj, 'Status', None)) if getattr(obj, 'Status', None) is not None else None
            self.Description = getattr(obj, 'Description', None)
            self.BankingOperationResult = BankingOperationResult(getattr(obj, 'BankingOperationResult', None)) if getattr(obj, 'BankingOperationResult', None) is not None else None
            self.BankDescription = getattr(obj, 'BankDescription', None)
            self.AccountName = getattr(obj, 'AccountName', None)
            self.AccoutPreview = getattr(obj, 'AccoutPreview', None)
            self.AccountType = PaymentMethodType(getattr(obj, 'AccountType', None)) if getattr(obj, 'AccountType', None) is not None else None
            self.TransactionDescription = getattr(obj, 'TransactionDescription', None)
            self.TransactionDueDate = getattr(obj, 'TransactionDueDate', None)
            self.LastModifiedDate = getattr(obj, 'LastModifiedDate', None)


