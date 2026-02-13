

from .TransactionIdentity import TransactionIdentity
from ..enums import BankingOperationResult
from ..enums import OperationStatus


class TransactionResultEntity(TransactionIdentity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.TransactionDescription = None
            self.BankingOperationResult = None
            self.BankingOperationDescription = None
            self.OperationStatus = None
            self.RealDueDate = None
            self.ProviderTransactionAdditionalInfos = None
            self.ProcessingFee = None
            self.ContainsPayoutData = None
            self.ProviderPayoutFeeAmount = None
            self.ProviderPayoutDepositAmount = None
            self.PayoutReportData = None
            self.ContainsPayoutReportData = None
            self.ForceCreateWebhookEvent = None

        else:
            super().__init__(obj)

            from .PayoutReportData import PayoutReportData
            self.TransactionDescription = getattr(obj, 'TransactionDescription', None)
            self.BankingOperationResult = BankingOperationResult(getattr(obj, 'BankingOperationResult', None)) if getattr(obj, 'BankingOperationResult', None) is not None else None
            self.BankingOperationDescription = getattr(obj, 'BankingOperationDescription', None)
            self.OperationStatus = OperationStatus(getattr(obj, 'OperationStatus', None)) if getattr(obj, 'OperationStatus', None) is not None else None
            self.RealDueDate = getattr(obj, 'RealDueDate', None)
            self.ProviderTransactionAdditionalInfos = getattr(obj, 'ProviderTransactionAdditionalInfos', None)
            self.ProcessingFee = getattr(obj, 'ProcessingFee', None)
            self.ContainsPayoutData = getattr(obj, 'ContainsPayoutData', None)
            self.ProviderPayoutFeeAmount = getattr(obj, 'ProviderPayoutFeeAmount', None)
            self.ProviderPayoutDepositAmount = getattr(obj, 'ProviderPayoutDepositAmount', None)
            self.PayoutReportData = PayoutReportData(getattr(obj, 'PayoutReportData', None)) if getattr(obj, 'PayoutReportData', None) is not None else None
            self.ContainsPayoutReportData = getattr(obj, 'ContainsPayoutReportData', None)
            self.ForceCreateWebhookEvent = getattr(obj, 'ForceCreateWebhookEvent', None)


