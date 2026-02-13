




class DeleteCustomerBulkArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.CustomerIds = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)

            self.CustomerIds = []
            if hasattr(obj, 'CustomerIds') and obj.CustomerIds is not None:
                self.CustomerIds = [name for name in obj.CustomerIds]


