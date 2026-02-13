




class ChangeTransactionStatusArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.TransactionId = None
            self.TransactionStatus = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.TransactionId = getattr(obj, 'TransactionId', None)
            self.TransactionStatus = getattr(obj, 'TransactionStatus', None)


