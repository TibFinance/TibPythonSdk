


from ..enums import OperationStatus
from ..enums import BankingOperationResult
from ..enums import Provider


class TransactionSatusResultEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.OperationStatus = None
            self.BankingOperationResult = None
            self.BankingOperationDescription = None
            self.ProviderType = None
            self.TransactionDescription = None
            self.ProviderTransactionId = None
            self.RealDueDate = None

        else:
            
            self.OperationStatus = OperationStatus(getattr(obj, 'OperationStatus', None)) if getattr(obj, 'OperationStatus', None) is not None else None
            self.BankingOperationResult = BankingOperationResult(getattr(obj, 'BankingOperationResult', None)) if getattr(obj, 'BankingOperationResult', None) is not None else None
            self.BankingOperationDescription = getattr(obj, 'BankingOperationDescription', None)
            self.ProviderType = Provider(getattr(obj, 'ProviderType', None)) if getattr(obj, 'ProviderType', None) is not None else None
            self.TransactionDescription = getattr(obj, 'TransactionDescription', None)
            self.ProviderTransactionId = getattr(obj, 'ProviderTransactionId', None)
            self.RealDueDate = getattr(obj, 'RealDueDate', None)


