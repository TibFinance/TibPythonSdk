
from ..utility import to_enum

from ..enums import Currency
from ..enums import OperationTarget
from ..enums import TransferDirection
from ..enums import OperationKind
from ..enums import TibOperationStatus


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
            self.Currency = to_enum(Currency, getattr(obj, 'Currency', None))
            self.OperationTarget = to_enum(OperationTarget, getattr(obj, 'OperationTarget', None))
            self.OperationDirection = to_enum(TransferDirection, getattr(obj, 'OperationDirection', None))
            self.OperationKind = to_enum(OperationKind, getattr(obj, 'OperationKind', None))
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.ExecutedDate = getattr(obj, 'ExecutedDate', None)

            self.Transactions = []
            if hasattr(obj, 'Transactions') and obj.Transactions is not None:
                self.Transactions = [TransactionCommon(name) for name in  obj.Transactions]
            self.OperationStatus = to_enum(TibOperationStatus, getattr(obj, 'OperationStatus', None))
            self.OverloadMerchantName = getattr(obj, 'OverloadMerchantName', None)


