




class GetDependentOperationArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.TransferId = None
            self.OperationId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.TransferId = getattr(obj, 'TransferId', None)
            self.OperationId = getattr(obj, 'OperationId', None)


