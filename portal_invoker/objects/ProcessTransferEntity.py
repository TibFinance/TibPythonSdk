


from ..enums import Currency
from ..enums import AcpOperationType
from ..enums import TransferDirection
from ..enums import Language
from ..enums import Provider


class ProcessTransferEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.TransactionId = None
            self.TransactionGroupId = None
            self.TransactionAmount = None
            self.Currency = None
            self.DueDate = None
            self.TransactionDescription = None
            self.AcpOperationType = None
            self.TransferDirection = None
            self.FavoriteProvider = None
            self.IsTransactionRevert = None
            self.AlreadyProcessedProviderId = None
            self.AlreadyProcessedProviderAdditionalInfos = None
            self.Language = None
            self.ProviderTransactionId = None
            self.ProviderSubType = None
            self.MerchantId = None
            self.ProviderType = None
            self.TransferId = None
            self.RelatedConvenientFeesWithTargetProviderId = None

        else:
            
            self.TransactionId = getattr(obj, 'TransactionId', None)
            self.TransactionGroupId = getattr(obj, 'TransactionGroupId', None)
            self.TransactionAmount = getattr(obj, 'TransactionAmount', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.DueDate = getattr(obj, 'DueDate', None)
            self.TransactionDescription = getattr(obj, 'TransactionDescription', None)
            self.AcpOperationType = AcpOperationType(getattr(obj, 'AcpOperationType', None)) if getattr(obj, 'AcpOperationType', None) is not None else None
            self.TransferDirection = TransferDirection(getattr(obj, 'TransferDirection', None)) if getattr(obj, 'TransferDirection', None) is not None else None
            self.FavoriteProvider = getattr(obj, 'FavoriteProvider', None)
            self.IsTransactionRevert = getattr(obj, 'IsTransactionRevert', None)
            self.AlreadyProcessedProviderId = getattr(obj, 'AlreadyProcessedProviderId', None)
            self.AlreadyProcessedProviderAdditionalInfos = getattr(obj, 'AlreadyProcessedProviderAdditionalInfos', None)
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.ProviderTransactionId = getattr(obj, 'ProviderTransactionId', None)
            self.ProviderSubType = getattr(obj, 'ProviderSubType', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.ProviderType = Provider(getattr(obj, 'ProviderType', None)) if getattr(obj, 'ProviderType', None) is not None else None
            self.TransferId = getattr(obj, 'TransferId', None)

            self.RelatedConvenientFeesWithTargetProviderId = []
            if hasattr(obj, 'RelatedConvenientFeesWithTargetProviderId') and obj.RelatedConvenientFeesWithTargetProviderId is not None:
                self.RelatedConvenientFeesWithTargetProviderId = [name for name in obj.RelatedConvenientFeesWithTargetProviderId]


