




class CreateTransactionFromRawArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.RawAcpFileContent = None
            self.MerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.RawAcpFileContent = getattr(obj, 'RawAcpFileContent', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


