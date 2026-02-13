




class RelaunchOperationBulkArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.OperationIds = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)

            self.OperationIds = []
            if hasattr(obj, 'OperationIds') and obj.OperationIds is not None:
                self.OperationIds = [name for name in obj.OperationIds]


