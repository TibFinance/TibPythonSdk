




class BoardingServiceMerchant:
    def __init__(self, obj=None):
        if obj is None:
            
            self.MerchantId = None
            self.BoardingInformationId = None
            self.BoardingStatus = None

        else:
            
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.BoardingInformationId = getattr(obj, 'BoardingInformationId', None)
            self.BoardingStatus = getattr(obj, 'BoardingStatus', None)


