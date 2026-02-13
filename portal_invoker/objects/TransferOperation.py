


from ..enums import Currency
from ..enums import OperationTarget
from ..enums import TransferDirection
from ..enums import OperationKind
from ..enums import TibOperationStatus


class TransferOperation:
    def __init__(self, obj=None):
        if obj is None:
            
            self.OperationId = None
            self.Amount = None
            self.Currency = None
            self.OperationTarget = None
            self.OperationDirection = None
            self.DependentOperation = None
            self.OperationKind = None
            self.ProcessDate = None
            self.OverloadedMerchantId = None
            self.OverloadedProviderId = None
            self.OperationStatus = None
            self.HasUsedWallet = None
            self.Transactions = None

        else:
            
            from .TransactionCommon import TransactionCommon
            self.OperationId = getattr(obj, 'OperationId', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.OperationTarget = OperationTarget(getattr(obj, 'OperationTarget', None)) if getattr(obj, 'OperationTarget', None) is not None else None
            self.OperationDirection = TransferDirection(getattr(obj, 'OperationDirection', None)) if getattr(obj, 'OperationDirection', None) is not None else None
            self.DependentOperation = getattr(obj, 'DependentOperation', None)
            self.OperationKind = OperationKind(getattr(obj, 'OperationKind', None)) if getattr(obj, 'OperationKind', None) is not None else None
            self.ProcessDate = getattr(obj, 'ProcessDate', None)
            self.OverloadedMerchantId = getattr(obj, 'OverloadedMerchantId', None)
            self.OverloadedProviderId = getattr(obj, 'OverloadedProviderId', None)
            self.OperationStatus = TibOperationStatus(getattr(obj, 'OperationStatus', None)) if getattr(obj, 'OperationStatus', None) is not None else None
            self.HasUsedWallet = getattr(obj, 'HasUsedWallet', None)

            self.Transactions = []
            if hasattr(obj, 'Transactions') and obj.Transactions is not None:
                self.Transactions = [TransactionCommon(name) for name in  obj.Transactions]


