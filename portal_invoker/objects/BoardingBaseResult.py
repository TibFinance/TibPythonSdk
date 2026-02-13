




class BoardingBaseResult:
    def __init__(self, obj=None):
        if obj is None:
            
            self.IsSuccess = None
            self.HttpStatusCode = None
            self.Message = None
            self.ErrorList = None

        else:
            
            from .BoardingBaseError import BoardingBaseError
            self.IsSuccess = getattr(obj, 'IsSuccess', None)
            self.HttpStatusCode = getattr(obj, 'HttpStatusCode', None)
            self.Message = getattr(obj, 'Message', None)

            self.ErrorList = []
            if hasattr(obj, 'ErrorList') and obj.ErrorList is not None:
                self.ErrorList = [BoardingBaseError(name) for name in  obj.ErrorList]


