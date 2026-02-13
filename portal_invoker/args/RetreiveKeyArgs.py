




class RetreiveKeyArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.EncryptionKey = None

        else:
            
            self.EncryptionKey = getattr(obj, 'EncryptionKey', None)


