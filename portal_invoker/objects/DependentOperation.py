




class DependentOperation:
    def __init__(self, obj=None):
        if obj is None:
            
            self.OperationId = None

        else:
            
            self.OperationId = getattr(obj, 'OperationId', None)


