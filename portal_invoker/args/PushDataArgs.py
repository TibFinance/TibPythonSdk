




class PushDataArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.DataCryptedBase64 = None

        else:
            
            self.DataCryptedBase64 = getattr(obj, 'DataCryptedBase64', None)


