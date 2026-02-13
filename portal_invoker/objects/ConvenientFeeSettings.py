


from ..enums import ConvenientFeeSettingStatus


class ConvenientFeeSettings:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ConvenientFeeSettingId = None
            self.MerchantId = None
            self.Percentage = None
            self.MinAmount = None
            self.MaxAmount = None
            self.FixedAmount = None
            self.PaymentMethodType = None
            self.TargetMerchantId = None
            self.Status = None

        else:
            
            self.ConvenientFeeSettingId = getattr(obj, 'ConvenientFeeSettingId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.Percentage = getattr(obj, 'Percentage', None)
            self.MinAmount = getattr(obj, 'MinAmount', None)
            self.MaxAmount = getattr(obj, 'MaxAmount', None)
            self.FixedAmount = getattr(obj, 'FixedAmount', None)
            self.PaymentMethodType = getattr(obj, 'PaymentMethodType', None)
            self.TargetMerchantId = getattr(obj, 'TargetMerchantId', None)
            self.Status = ConvenientFeeSettingStatus(getattr(obj, 'Status', None)) if getattr(obj, 'Status', None) is not None else None


