




class ServiceWithMerchant:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ServicePrimaryMerchant = None
            self.ServiceFeeSettings = None
            self.ServiceSettings = None
            self.OverloadedFeesMerchantName = None

        else:
            
            from .MerchantView import MerchantView
            from .ServiceFeeSettings import ServiceFeeSettings
            from .ServiceSettings import ServiceSettings
            self.ServicePrimaryMerchant = MerchantView(getattr(obj, 'ServicePrimaryMerchant', None)) if getattr(obj, 'ServicePrimaryMerchant', None) is not None else None
            self.ServiceFeeSettings = ServiceFeeSettings(getattr(obj, 'ServiceFeeSettings', None)) if getattr(obj, 'ServiceFeeSettings', None) is not None else None
            self.ServiceSettings = ServiceSettings(getattr(obj, 'ServiceSettings', None)) if getattr(obj, 'ServiceSettings', None) is not None else None
            self.OverloadedFeesMerchantName = getattr(obj, 'OverloadedFeesMerchantName', None)


