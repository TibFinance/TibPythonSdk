


from ..enums import OperationKind
from ..enums import PaymentMethodType


class FeeReportLineItem:
    def __init__(self, obj=None):
        if obj is None:
            
            self.OperationId = None
            self.TransferId = None
            self.CreatedDate = None
            self.ExecutedDate = None
            self.Amount = None
            self.Currency = None
            self.FeeType = None
            self.FeeTypeDescription = None
            self.PaymentMethodType = None
            self.PaymentMethodTypeDescription = None
            self.MerchantName = None
            self.MerchantId = None
            self.CustomerName = None
            self.TransferExternalReference = None
            self.OperationStatus = None

        else:
            
            self.OperationId = getattr(obj, 'OperationId', None)
            self.TransferId = getattr(obj, 'TransferId', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.ExecutedDate = getattr(obj, 'ExecutedDate', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.Currency = getattr(obj, 'Currency', None)
            self.FeeType = OperationKind(getattr(obj, 'FeeType', None)) if getattr(obj, 'FeeType', None) is not None else None
            self.FeeTypeDescription = getattr(obj, 'FeeTypeDescription', None)
            self.PaymentMethodType = PaymentMethodType(getattr(obj, 'PaymentMethodType', None)) if getattr(obj, 'PaymentMethodType', None) is not None else None
            self.PaymentMethodTypeDescription = getattr(obj, 'PaymentMethodTypeDescription', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.CustomerName = getattr(obj, 'CustomerName', None)
            self.TransferExternalReference = getattr(obj, 'TransferExternalReference', None)
            self.OperationStatus = getattr(obj, 'OperationStatus', None)


