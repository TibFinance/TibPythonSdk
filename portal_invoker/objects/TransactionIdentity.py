

from .ProviderTransactionIdentity import ProviderTransactionIdentity
from ..enums import Currency


class TransactionIdentity(ProviderTransactionIdentity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.TransactionId = None
            self.RelatedMerchantId = None
            self.LastExecutionDescription = None
            self.TransactionAmount = None
            self.OriginalTransactionDueDatePassedWeekend = None
            self.OriginalTransactionCreatedDatePassedWeekend = None
            self.Currency = None
            self.TransferId = None
            self.PayoutId = None

        else:
            super().__init__(obj)

            self.TransactionId = getattr(obj, 'TransactionId', None)
            self.RelatedMerchantId = getattr(obj, 'RelatedMerchantId', None)
            self.LastExecutionDescription = getattr(obj, 'LastExecutionDescription', None)
            self.TransactionAmount = getattr(obj, 'TransactionAmount', None)
            self.OriginalTransactionDueDatePassedWeekend = getattr(obj, 'OriginalTransactionDueDatePassedWeekend', None)
            self.OriginalTransactionCreatedDatePassedWeekend = getattr(obj, 'OriginalTransactionCreatedDatePassedWeekend', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.TransferId = getattr(obj, 'TransferId', None)
            self.PayoutId = getattr(obj, 'PayoutId', None)


