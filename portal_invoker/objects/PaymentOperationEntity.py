


from ..enums import Currency
from ..enums import OperationTarget
from ..enums import TransferDirection
from ..enums import OperationKind


class PaymentOperationEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Amount = None
            self.Currency = None
            self.OperationTarget = None
            self.OperationDirection = None
            self.OperationKind = None
            self.CreatedDate = None
            self.ExecutedDate = None
            self.Transactions = None
            self.OperationStatus = None
            self.OverloadMerchantName = None

        else:
            
            from .TransactionCommon import TransactionCommon
            self.Amount = getattr(obj, 'Amount', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.OperationTarget = OperationTarget(getattr(obj, 'OperationTarget', None)) if getattr(obj, 'OperationTarget', None) is not None else None
            self.OperationDirection = TransferDirection(getattr(obj, 'OperationDirection', None)) if getattr(obj, 'OperationDirection', None) is not None else None
            self.OperationKind = OperationKind(getattr(obj, 'OperationKind', None)) if getattr(obj, 'OperationKind', None) is not None else None
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.ExecutedDate = getattr(obj, 'ExecutedDate', None)

            self.Transactions = []
            if hasattr(obj, 'Transactions') and obj.Transactions is not None:
                self.Transactions = [TransactionCommon(name) for name in  obj.Transactions]
            self.OperationStatus = getattr(obj, 'OperationStatus', None)
            self.OverloadMerchantName = getattr(obj, 'OverloadMerchantName', None)


