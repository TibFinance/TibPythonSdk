




class CreateTransactionFromRawArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.RawAcpFileContent = None
            self.MerchantId = None
            self.IsImmediate = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.RawAcpFileContent = getattr(obj, 'RawAcpFileContent', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.IsImmediate = getattr(obj, 'IsImmediate', None)


