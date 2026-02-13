




class GetBoardingMerchantStatusEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ProviderMerchantId = None

        else:
            
            self.ProviderMerchantId = getattr(obj, 'ProviderMerchantId', None)


