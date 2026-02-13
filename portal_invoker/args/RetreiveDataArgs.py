




class RetreiveDataArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.DataId = None

        else:
            
            self.DataId = getattr(obj, 'DataId', None)


