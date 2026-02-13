


from ..enums import Currency
from ..enums import OperationTarget
from ..enums import TransferDirection
from ..enums import OperationKind
from ..enums import TibOperationStatus
from ..enums import AcpOperationType


class AdminOperation:
    def __init__(self, obj=None):
        if obj is None:
            
            self.OperationId = None
            self.TransferId = None
            self.OperationTypeRef = None
            self.Amount = None
            self.Currency = None
            self.OperationTarget = None
            self.OperationDirection = None
            self.DependentOperationId = None
            self.TransactionGroupId = None
            self.OperationKind = None
            self.CreatedDate = None
            self.ExecutedDate = None
            self.ProcessDate = None
            self.OperationsGroupId = None
            self.OperationStatus = None
            self.RevertProviderTransactionId = None
            self.OverloadedMerchantId = None
            self.IsArchived = None
            self.RevertProviderId = None
            self.RevertProviderTransactionAdditionalInfos = None
            self.RelatedMerchantId = None
            self.RelatedCustomerId = None
            self.IsChecked = None
            self.AcpTransactionType = None
            self.OperationTargetValue = None
            self.CurrencyValue = None
            self.OperationDirectionValue = None
            self.OperationStatusValue = None
            self.OperationKindValue = None
            self.AcpTransactionTypeValue = None

        else:
            
            self.OperationId = getattr(obj, 'OperationId', None)
            self.TransferId = getattr(obj, 'TransferId', None)
            self.OperationTypeRef = getattr(obj, 'OperationTypeRef', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.OperationTarget = OperationTarget(getattr(obj, 'OperationTarget', None)) if getattr(obj, 'OperationTarget', None) is not None else None
            self.OperationDirection = TransferDirection(getattr(obj, 'OperationDirection', None)) if getattr(obj, 'OperationDirection', None) is not None else None
            self.DependentOperationId = getattr(obj, 'DependentOperationId', None)
            self.TransactionGroupId = getattr(obj, 'TransactionGroupId', None)
            self.OperationKind = OperationKind(getattr(obj, 'OperationKind', None)) if getattr(obj, 'OperationKind', None) is not None else None
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.ExecutedDate = getattr(obj, 'ExecutedDate', None)
            self.ProcessDate = getattr(obj, 'ProcessDate', None)
            self.OperationsGroupId = getattr(obj, 'OperationsGroupId', None)
            self.OperationStatus = TibOperationStatus(getattr(obj, 'OperationStatus', None)) if getattr(obj, 'OperationStatus', None) is not None else None
            self.RevertProviderTransactionId = getattr(obj, 'RevertProviderTransactionId', None)
            self.OverloadedMerchantId = getattr(obj, 'OverloadedMerchantId', None)
            self.IsArchived = getattr(obj, 'IsArchived', None)
            self.RevertProviderId = getattr(obj, 'RevertProviderId', None)
            self.RevertProviderTransactionAdditionalInfos = getattr(obj, 'RevertProviderTransactionAdditionalInfos', None)
            self.RelatedMerchantId = getattr(obj, 'RelatedMerchantId', None)
            self.RelatedCustomerId = getattr(obj, 'RelatedCustomerId', None)
            self.IsChecked = getattr(obj, 'IsChecked', None)
            self.AcpTransactionType = AcpOperationType(getattr(obj, 'AcpTransactionType', None)) if getattr(obj, 'AcpTransactionType', None) is not None else None
            self.OperationTargetValue = getattr(obj, 'OperationTargetValue', None)
            self.CurrencyValue = getattr(obj, 'CurrencyValue', None)
            self.OperationDirectionValue = getattr(obj, 'OperationDirectionValue', None)
            self.OperationStatusValue = getattr(obj, 'OperationStatusValue', None)
            self.OperationKindValue = getattr(obj, 'OperationKindValue', None)
            self.AcpTransactionTypeValue = getattr(obj, 'AcpTransactionTypeValue', None)


