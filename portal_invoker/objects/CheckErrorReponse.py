




class CheckErrorReponse:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CheckResult = None
            self.Result = None

        else:
            
            from .CheckResult import CheckResult
            from .CheckResultDetail import CheckResultDetail
            self.CheckResult = CheckResult(getattr(obj, 'CheckResult', None)) if getattr(obj, 'CheckResult', None) is not None else None

            self.Result = []
            if hasattr(obj, 'Result') and obj.Result is not None:
                self.Result = [CheckResultDetail(name) for name in  obj.Result]


