




class ChangeOperationStatusBulkArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.OperationIds = None
            self.OperationStatus = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)

            self.OperationIds = []
            if hasattr(obj, 'OperationIds') and obj.OperationIds is not None:
                self.OperationIds = [name for name in obj.OperationIds]
            self.OperationStatus = getattr(obj, 'OperationStatus', None)


