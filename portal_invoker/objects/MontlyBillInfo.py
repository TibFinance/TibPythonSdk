


from ..enums import Language
from ..enums import OperationKind
from ..enums import PaymentMethodType


class MontlyBillInfo:
    def __init__(self, obj=None):
        if obj is None:
            
            self.MerchantName = None
            self.MerchantLanguage = None
            self.OperationKind = None
            self.TotalAmount = None
            self.TotalCount = None
            self.PaymentMethodType = None
            self.MerchantId = None

        else:
            
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.MerchantLanguage = Language(getattr(obj, 'MerchantLanguage', None)) if getattr(obj, 'MerchantLanguage', None) is not None else None
            self.OperationKind = OperationKind(getattr(obj, 'OperationKind', None)) if getattr(obj, 'OperationKind', None) is not None else None
            self.TotalAmount = getattr(obj, 'TotalAmount', None)
            self.TotalCount = getattr(obj, 'TotalCount', None)
            self.PaymentMethodType = PaymentMethodType(getattr(obj, 'PaymentMethodType', None)) if getattr(obj, 'PaymentMethodType', None) is not None else None
            self.MerchantId = getattr(obj, 'MerchantId', None)


