


from ..enums import Currency
from ..enums import TransferDirection
from ..enums import OperationKind
from ..enums import ProcessStatus


class FreeCollectionWithHierarchy:
    def __init__(self, obj=None):
        if obj is None:
            
            self.FreeCollectionId = None
            self.MerchantId = None
            self.Currency = None
            self.OperationDirection = None
            self.OperationKind = None
            self.Amount = None
            self.OperationAmount = None
            self.CurrentStatus = None
            self.CreatedDate = None
            self.AccountName = None
            self.ReferenceId = None
            self.ExecutedDate = None
            self.TransferDueDate = None
            self.PaymentMethodType = None

        else:
            
            self.FreeCollectionId = getattr(obj, 'FreeCollectionId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.OperationDirection = TransferDirection(getattr(obj, 'OperationDirection', None)) if getattr(obj, 'OperationDirection', None) is not None else None
            self.OperationKind = OperationKind(getattr(obj, 'OperationKind', None)) if getattr(obj, 'OperationKind', None) is not None else None
            self.Amount = getattr(obj, 'Amount', None)
            self.OperationAmount = getattr(obj, 'OperationAmount', None)
            self.CurrentStatus = ProcessStatus(getattr(obj, 'CurrentStatus', None)) if getattr(obj, 'CurrentStatus', None) is not None else None
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.AccountName = getattr(obj, 'AccountName', None)
            self.ReferenceId = getattr(obj, 'ReferenceId', None)
            self.ExecutedDate = getattr(obj, 'ExecutedDate', None)
            self.TransferDueDate = getattr(obj, 'TransferDueDate', None)
            self.PaymentMethodType = getattr(obj, 'PaymentMethodType', None)


