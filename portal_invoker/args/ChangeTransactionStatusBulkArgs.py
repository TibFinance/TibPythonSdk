




class ChangeTransactionStatusBulkArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.TransactionIds = None
            self.TransactionStatus = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)

            self.TransactionIds = []
            if hasattr(obj, 'TransactionIds') and obj.TransactionIds is not None:
                self.TransactionIds = [name for name in obj.TransactionIds]
            self.TransactionStatus = getattr(obj, 'TransactionStatus', None)


