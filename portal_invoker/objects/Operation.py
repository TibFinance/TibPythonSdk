


from ..enums import Currency
from ..enums import OperationTarget
from ..enums import TransferDirection


class Operation:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Amount = None
            self.Currency = None
            self.OperationTarget = None
            self.OperationDirection = None
            self.PaymentOrMerchantId = None
            self.Transactions = None
            self.OperationRelatedPayments = None

        else:
            
            from .TransactionCommon import TransactionCommon
            from .PaymentOperationWithHierarchy import PaymentOperationWithHierarchy
            self.Amount = getattr(obj, 'Amount', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.OperationTarget = OperationTarget(getattr(obj, 'OperationTarget', None)) if getattr(obj, 'OperationTarget', None) is not None else None
            self.OperationDirection = TransferDirection(getattr(obj, 'OperationDirection', None)) if getattr(obj, 'OperationDirection', None) is not None else None
            self.PaymentOrMerchantId = getattr(obj, 'PaymentOrMerchantId', None)

            self.Transactions = []
            if hasattr(obj, 'Transactions') and obj.Transactions is not None:
                self.Transactions = [TransactionCommon(name) for name in  obj.Transactions]

            self.OperationRelatedPayments = []
            if hasattr(obj, 'OperationRelatedPayments') and obj.OperationRelatedPayments is not None:
                self.OperationRelatedPayments = [PaymentOperationWithHierarchy(name) for name in  obj.OperationRelatedPayments]


