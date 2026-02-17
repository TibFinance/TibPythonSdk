


from ..enums import PaymentMethodType


class PaymentMethod:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PaymentMethodId = None
            self.IsCustomerAutomaticPaymentMethod = None
            self.PaymentMethodType = None
            self.PaymentMethodDescription = None
            self.AccountPreview = None
            self.ExpirationDate = None
            self.Owner = None
            self.CcType = None
            self.PreauthorizedMerchants = None

        else:
            
            from .MerchantIdName import MerchantIdName
            self.PaymentMethodId = getattr(obj, 'PaymentMethodId', None)
            self.IsCustomerAutomaticPaymentMethod = getattr(obj, 'IsCustomerAutomaticPaymentMethod', None)
            self.PaymentMethodType = PaymentMethodType(getattr(obj, 'PaymentMethodType', None)) if getattr(obj, 'PaymentMethodType', None) is not None else None
            self.PaymentMethodDescription = getattr(obj, 'PaymentMethodDescription', None)
            self.AccountPreview = getattr(obj, 'AccountPreview', None)
            self.ExpirationDate = getattr(obj, 'ExpirationDate', None)
            self.Owner = getattr(obj, 'Owner', None)
            self.CcType = getattr(obj, 'CcType', None)

            self.PreauthorizedMerchants = []
            if hasattr(obj, 'PreauthorizedMerchants') and obj.PreauthorizedMerchants is not None:
                self.PreauthorizedMerchants = [MerchantIdName(name) for name in  obj.PreauthorizedMerchants]


