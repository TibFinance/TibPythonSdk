


from ..enums import Currency
from ..enums import OperationTarget
from ..enums import TransferDirection


class AdminTranGroup:
    def __init__(self, obj=None):
        if obj is None:
            
            self.TransactionGroupId = None
            self.Amount = None
            self.Currency = None
            self.TargetSystemId = None
            self.OperationTarget = None
            self.BaseOperationDirection = None
            self.RelatedMerchantId = None
            self.OperationId = None
            self.TransferId = None
            self.RelatedCustomerId = None
            self.IsChecked = None
            self.MerchantIds = None
            self.CustomerIds = None
            self.TransferIds = None
            self.OperationIds = None
            self.OperationTargetValue = None
            self.CurrencyValue = None
            self.BaseOperationDirectionValue = None

        else:
            
            self.TransactionGroupId = getattr(obj, 'TransactionGroupId', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.TargetSystemId = getattr(obj, 'TargetSystemId', None)
            self.OperationTarget = OperationTarget(getattr(obj, 'OperationTarget', None)) if getattr(obj, 'OperationTarget', None) is not None else None
            self.BaseOperationDirection = TransferDirection(getattr(obj, 'BaseOperationDirection', None)) if getattr(obj, 'BaseOperationDirection', None) is not None else None
            self.RelatedMerchantId = getattr(obj, 'RelatedMerchantId', None)
            self.OperationId = getattr(obj, 'OperationId', None)
            self.TransferId = getattr(obj, 'TransferId', None)
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
            self.OperationTargetValue = getattr(obj, 'OperationTargetValue', None)
            self.CurrencyValue = getattr(obj, 'CurrencyValue', None)
            self.BaseOperationDirectionValue = getattr(obj, 'BaseOperationDirectionValue', None)


