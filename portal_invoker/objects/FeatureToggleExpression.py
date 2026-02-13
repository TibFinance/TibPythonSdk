




class FeatureToggleExpression:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ClientId = None
            self.ServiceIds = None
            self.MerchantIds = None

        else:
            
            self.ClientId = getattr(obj, 'ClientId', None)

            self.ServiceIds = []
            if hasattr(obj, 'ServiceIds') and obj.ServiceIds is not None:
                self.ServiceIds = [name for name in obj.ServiceIds]

            self.MerchantIds = []
            if hasattr(obj, 'MerchantIds') and obj.MerchantIds is not None:
                self.MerchantIds = [name for name in obj.MerchantIds]


