




class ExternallyCryptedDataEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ExternalKeyId = None
            self.ExternalVaultId = None
            self.EncryptionIV = None
            self.CryptedDataPart1 = None

        else:
            
            self.ExternalKeyId = getattr(obj, 'ExternalKeyId', None)
            self.ExternalVaultId = getattr(obj, 'ExternalVaultId', None)
            self.EncryptionIV = getattr(obj, 'EncryptionIV', None)
            self.CryptedDataPart1 = getattr(obj, 'CryptedDataPart1', None)


