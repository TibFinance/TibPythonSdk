




class SaveProviderMerchantArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ProviderMerchantId = None
            self.BoardingInformationId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ProviderMerchantId = getattr(obj, 'ProviderMerchantId', None)
            self.BoardingInformationId = getattr(obj, 'BoardingInformationId', None)


