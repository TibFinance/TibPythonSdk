




class SESARWebHookArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CryptedObject = None
            self.HashKey = None

        else:
            
            self.CryptedObject = getattr(obj, 'CryptedObject', None)
            self.HashKey = getattr(obj, 'HashKey', None)


