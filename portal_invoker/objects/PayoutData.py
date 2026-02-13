




class PayoutData:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Paid = None
            self.Date = None
            self.Gross = None
            self.Fees = None

        else:
            
            self.Paid = getattr(obj, 'Paid', None)
            self.Date = getattr(obj, 'Date', None)
            self.Gross = getattr(obj, 'Gross', None)
            self.Fees = getattr(obj, 'Fees', None)


