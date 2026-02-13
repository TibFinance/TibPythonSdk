




class BatchFileEventToBroadcast:
    def __init__(self, obj=None):
        if obj is None:
            
            self.FreeOperation = None
            self.File = None
            self.PaymentId = None

        else:
            
            from .FreeOperation import FreeOperation
            self.FreeOperation = FreeOperation(getattr(obj, 'FreeOperation', None)) if getattr(obj, 'FreeOperation', None) is not None else None
            self.File = getattr(obj, 'File', None)
            self.PaymentId = getattr(obj, 'PaymentId', None)


