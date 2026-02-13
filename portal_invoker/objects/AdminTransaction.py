


from ..enums import OperationType
from ..enums import TransferDirection
from ..enums import OperationStatus
from ..enums import AccountType
from ..enums import AcpOperationType
from ..enums import OperationKind


class AdminTransaction:
    def __init__(self, obj=None):
        if obj is None:
            
            self.TransactionId = None
            self.TransactionGroupId = None
            self.OperationType = None
            self.OperationDirection = None
            self.OperationStatus = None
            self.Description = None
            self.DescriptionCode = None
            self.ProviderTransactionId = None
            self.ProviderTransactionGroupId = None
            self.CreatedDate = None
            self.NextStepTransaction = None
            self.AccountName = None
            self.AccoutPreview = None
            self.AccountInformationId = None
            self.AccountType = None
            self.TransactionDescription = None
            self.TransactionDueDate = None
            self.AcpTransactionType = None
            self.ReceivedDescription = None
            self.RealDueDate = None
            self.DueDateUpdatedDate = None
            self.ProcessExecuted = None
            self.LastModifiedDate = None
            self.ExportBeenExecuted = None
            self.IsRevert = None
            self.IsArchived = None
            self.FavoriteProviderId = None
            self.ExecutedByProviderId = None
            self.OperationKind = None
            self.ProviderTransactionAdditionalInfos = None
            self.OperationId = None
            self.TransferId = None
            self.RelatedMerchantId = None
            self.RelatedCustomerId = None
            self.IsChecked = None
            self.MerchantIds = None
            self.CustomerIds = None
            self.TransferIds = None
            self.OperationIds = None
            self.OperationTypeValue = None
            self.OperationDirectionValue = None
            self.OperationStatusValue = None
            self.OperationKindValue = None
            self.AccountTypeValue = None
            self.AcpTransactionTypeValue = None

        else:
            
            self.TransactionId = getattr(obj, 'TransactionId', None)
            self.TransactionGroupId = getattr(obj, 'TransactionGroupId', None)
            self.OperationType = OperationType(getattr(obj, 'OperationType', None)) if getattr(obj, 'OperationType', None) is not None else None
            self.OperationDirection = TransferDirection(getattr(obj, 'OperationDirection', None)) if getattr(obj, 'OperationDirection', None) is not None else None
            self.OperationStatus = OperationStatus(getattr(obj, 'OperationStatus', None)) if getattr(obj, 'OperationStatus', None) is not None else None
            self.Description = getattr(obj, 'Description', None)
            self.DescriptionCode = getattr(obj, 'DescriptionCode', None)
            self.ProviderTransactionId = getattr(obj, 'ProviderTransactionId', None)
            self.ProviderTransactionGroupId = getattr(obj, 'ProviderTransactionGroupId', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.NextStepTransaction = getattr(obj, 'NextStepTransaction', None)
            self.AccountName = getattr(obj, 'AccountName', None)
            self.AccoutPreview = getattr(obj, 'AccoutPreview', None)
            self.AccountInformationId = getattr(obj, 'AccountInformationId', None)
            self.AccountType = AccountType(getattr(obj, 'AccountType', None)) if getattr(obj, 'AccountType', None) is not None else None
            self.TransactionDescription = getattr(obj, 'TransactionDescription', None)
            self.TransactionDueDate = getattr(obj, 'TransactionDueDate', None)
            self.AcpTransactionType = AcpOperationType(getattr(obj, 'AcpTransactionType', None)) if getattr(obj, 'AcpTransactionType', None) is not None else None
            self.ReceivedDescription = getattr(obj, 'ReceivedDescription', None)
            self.RealDueDate = getattr(obj, 'RealDueDate', None)
            self.DueDateUpdatedDate = getattr(obj, 'DueDateUpdatedDate', None)
            self.ProcessExecuted = getattr(obj, 'ProcessExecuted', None)
            self.LastModifiedDate = getattr(obj, 'LastModifiedDate', None)
            self.ExportBeenExecuted = getattr(obj, 'ExportBeenExecuted', None)
            self.IsRevert = getattr(obj, 'IsRevert', None)
            self.IsArchived = getattr(obj, 'IsArchived', None)
            self.FavoriteProviderId = getattr(obj, 'FavoriteProviderId', None)
            self.ExecutedByProviderId = getattr(obj, 'ExecutedByProviderId', None)
            self.OperationKind = OperationKind(getattr(obj, 'OperationKind', None)) if getattr(obj, 'OperationKind', None) is not None else None
            self.ProviderTransactionAdditionalInfos = getattr(obj, 'ProviderTransactionAdditionalInfos', None)
            self.OperationId = getattr(obj, 'OperationId', None)
            self.TransferId = getattr(obj, 'TransferId', None)
            self.RelatedMerchantId = getattr(obj, 'RelatedMerchantId', None)
            self.RelatedCustomerId = getattr(obj, 'RelatedCustomerId', None)
            self.IsChecked = getattr(obj, 'IsChecked', None)

            self.MerchantIds = []
            if hasattr(obj, 'MerchantIds') and obj.MerchantIds is not None:
                self.MerchantIds = [name for name in obj.MerchantIds]

            self.CustomerIds = []
            if hasattr(obj, 'CustomerIds') and obj.CustomerIds is not None:
                self.CustomerIds = [name for name in obj.CustomerIds]

            self.TransferIds = []
            if hasattr(obj, 'TransferIds') and obj.TransferIds is not None:
                self.TransferIds = [name for name in obj.TransferIds]

            self.OperationIds = []
            if hasattr(obj, 'OperationIds') and obj.OperationIds is not None:
                self.OperationIds = [name for name in obj.OperationIds]
            self.OperationTypeValue = getattr(obj, 'OperationTypeValue', None)
            self.OperationDirectionValue = getattr(obj, 'OperationDirectionValue', None)
            self.OperationStatusValue = getattr(obj, 'OperationStatusValue', None)
            self.OperationKindValue = getattr(obj, 'OperationKindValue', None)
            self.AccountTypeValue = getattr(obj, 'AccountTypeValue', None)
            self.AcpTransactionTypeValue = getattr(obj, 'AcpTransactionTypeValue', None)


