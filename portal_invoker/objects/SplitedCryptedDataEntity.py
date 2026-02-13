




class SplitedCryptedDataEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Base64CryptedDataPart1 = None
            self.Base64CryptedDataPart2 = None

        else:
            
            self.Base64CryptedDataPart1 = getattr(obj, 'Base64CryptedDataPart1', None)
            self.Base64CryptedDataPart2 = getattr(obj, 'Base64CryptedDataPart2', None)


