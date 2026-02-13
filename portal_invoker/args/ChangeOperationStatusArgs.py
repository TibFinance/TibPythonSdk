




class ChangeOperationStatusArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.OperationId = None
            self.OperationStatus = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.OperationId = getattr(obj, 'OperationId', None)
            self.OperationStatus = getattr(obj, 'OperationStatus', None)


