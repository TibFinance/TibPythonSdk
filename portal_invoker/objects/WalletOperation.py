




class WalletOperation:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Date = None
            self.Amount = None
            self.IsWithdrawn = None
            self.Description = None

        else:
            
            self.Date = getattr(obj, 'Date', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.IsWithdrawn = getattr(obj, 'IsWithdrawn', None)
            self.Description = getattr(obj, 'Description', None)


