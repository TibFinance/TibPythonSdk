




class DoesClientExistArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ClientId = None

        else:
            
            self.ClientId = getattr(obj, 'ClientId', None)


