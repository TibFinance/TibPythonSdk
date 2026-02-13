




class DeleteServiceBulkArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.ServiceIds = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)

            self.ServiceIds = []
            if hasattr(obj, 'ServiceIds') and obj.ServiceIds is not None:
                self.ServiceIds = [name for name in obj.ServiceIds]


