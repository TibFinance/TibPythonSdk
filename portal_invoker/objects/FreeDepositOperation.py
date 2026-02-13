


from ..enums import Currency
from ..enums import OperationTarget
from ..enums import TransferDirection


class FreeDepositOperation:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Amount = None
            self.Currency = None
            self.OperationTarget = None
            self.OperationDirection = None
            self.TargetSystemId = None
            self.Transactions = None
            self.FreeDepositList = None

        else:
            
            from .TransactionCommon import TransactionCommon
            from .FreeDepositWithHierarchy import FreeDepositWithHierarchy
            self.Amount = getattr(obj, 'Amount', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.OperationTarget = OperationTarget(getattr(obj, 'OperationTarget', None)) if getattr(obj, 'OperationTarget', None) is not None else None
            self.OperationDirection = TransferDirection(getattr(obj, 'OperationDirection', None)) if getattr(obj, 'OperationDirection', None) is not None else None
            self.TargetSystemId = getattr(obj, 'TargetSystemId', None)

            self.Transactions = []
            if hasattr(obj, 'Transactions') and obj.Transactions is not None:
                self.Transactions = [TransactionCommon(name) for name in  obj.Transactions]

            self.FreeDepositList = []
            if hasattr(obj, 'FreeDepositList') and obj.FreeDepositList is not None:
                self.FreeDepositList = [FreeDepositWithHierarchy(name) for name in  obj.FreeDepositList]


