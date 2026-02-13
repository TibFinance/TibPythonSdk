




class CashBackStats:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Date = None
            self.Count = None
            self.Amount = None

        else:
            
            self.Date = getattr(obj, 'Date', None)
            self.Count = getattr(obj, 'Count', None)
            self.Amount = getattr(obj, 'Amount', None)


