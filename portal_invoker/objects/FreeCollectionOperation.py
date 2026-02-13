


from ..enums import Currency
from ..enums import OperationTarget
from ..enums import TransferDirection


class FreeCollectionOperation:
    def __init__(self, obj=None):
        if obj is None:
            
            self.OperationTypeRef = None
            self.Amount = None
            self.Currency = None
            self.OperationTarget = None
            self.OperationDirection = None
            self.TargetSystemId = None
            self.Transactions = None
            self.FreeCollectionList = None

        else:
            
            from .TransactionCommon import TransactionCommon
            from .FreeCollectionWithHierarchy import FreeCollectionWithHierarchy
            self.OperationTypeRef = getattr(obj, 'OperationTypeRef', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.OperationTarget = OperationTarget(getattr(obj, 'OperationTarget', None)) if getattr(obj, 'OperationTarget', None) is not None else None
            self.OperationDirection = TransferDirection(getattr(obj, 'OperationDirection', None)) if getattr(obj, 'OperationDirection', None) is not None else None
            self.TargetSystemId = getattr(obj, 'TargetSystemId', None)

            self.Transactions = []
            if hasattr(obj, 'Transactions') and obj.Transactions is not None:
                self.Transactions = [TransactionCommon(name) for name in  obj.Transactions]

            self.FreeCollectionList = []
            if hasattr(obj, 'FreeCollectionList') and obj.FreeCollectionList is not None:
                self.FreeCollectionList = [FreeCollectionWithHierarchy(name) for name in  obj.FreeCollectionList]


