


from ..enums import TransferFrequency
from ..enums import TransferType


class RecuringTransfer:
    def __init__(self, obj=None):
        if obj is None:
            
            self.NextRecuringDate = None
            self.RecuringTransferId = None
            self.RecuringMode = None
            self.TransferType = None
            self.RelatedPaymentMethodId = None
            self.RecuringRefDate = None
            self.CreatedDate = None
            self.RelatedMerchantId = None
            self.RelatedMerchantName = None
            self.CustomerName = None
            self.CustomerId = None
            self.Amount = None
            self.TrasnferTitle = None
            self.TrasnferDescription = None
            self.TrasnferExternalSystemNumber = None

        else:
            
            self.NextRecuringDate = getattr(obj, 'NextRecuringDate', None)
            self.RecuringTransferId = getattr(obj, 'RecuringTransferId', None)
            self.RecuringMode = TransferFrequency(getattr(obj, 'RecuringMode', None)) if getattr(obj, 'RecuringMode', None) is not None else None
            self.TransferType = TransferType(getattr(obj, 'TransferType', None)) if getattr(obj, 'TransferType', None) is not None else None
            self.RelatedPaymentMethodId = getattr(obj, 'RelatedPaymentMethodId', None)
            self.RecuringRefDate = getattr(obj, 'RecuringRefDate', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.RelatedMerchantId = getattr(obj, 'RelatedMerchantId', None)
            self.RelatedMerchantName = getattr(obj, 'RelatedMerchantName', None)
            self.CustomerName = getattr(obj, 'CustomerName', None)
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.TrasnferTitle = getattr(obj, 'TrasnferTitle', None)
            self.TrasnferDescription = getattr(obj, 'TrasnferDescription', None)
            self.TrasnferExternalSystemNumber = getattr(obj, 'TrasnferExternalSystemNumber', None)


