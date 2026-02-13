




class CheckResult:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AccountFound = None
            self.FromDate = None
            self.ToDate = None
            self.FailCount = None

        else:
            
            self.AccountFound = getattr(obj, 'AccountFound', None)
            self.FromDate = getattr(obj, 'FromDate', None)
            self.ToDate = getattr(obj, 'ToDate', None)
            self.FailCount = getattr(obj, 'FailCount', None)


