
from ..utility import to_enum
from .BaseApiResponse import BaseApiResponse
from ..enums import TransferType
from ..enums import Language


class RequestDataResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.MerchantId = None
            self.Amount = None
            self.CustomerId = None
            self.PaymentMethodId = None
            self.TransferType = None
            self.ReferenceNumber = None
            self.Language = None
            self.TransactionDueDate = None

        else:
            super().__init__(obj)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.PaymentMethodId = getattr(obj, 'PaymentMethodId', None)
            self.TransferType = to_enum(TransferType, getattr(obj, 'TransferType', None))
            self.ReferenceNumber = getattr(obj, 'ReferenceNumber', None)
            self.Language = to_enum(Language, getattr(obj, 'Language', None))
            self.TransactionDueDate = getattr(obj, 'TransactionDueDate', None)


