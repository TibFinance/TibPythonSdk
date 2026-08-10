
from ..utility import to_enum

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
            self.EndDate = None
            self.IsSupplierTransfer = None
            self.PayerMerchantName = None
            self.IsCurrentUserPayer = None

        else:
            
            self.NextRecuringDate = getattr(obj, 'NextRecuringDate', None)
            self.RecuringTransferId = getattr(obj, 'RecuringTransferId', None)
            self.RecuringMode = to_enum(TransferFrequency, getattr(obj, 'RecuringMode', None))
            self.TransferType = to_enum(TransferType, getattr(obj, 'TransferType', None))
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
            self.EndDate = getattr(obj, 'EndDate', None)
            self.IsSupplierTransfer = getattr(obj, 'IsSupplierTransfer', None)
            self.PayerMerchantName = getattr(obj, 'PayerMerchantName', None)
            self.IsCurrentUserPayer = getattr(obj, 'IsCurrentUserPayer', None)


