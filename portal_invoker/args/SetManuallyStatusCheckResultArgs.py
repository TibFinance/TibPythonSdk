


from ..enums import OperationStatus


class SetManuallyStatusCheckResultArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.TransactionId = None
            self.OperationStatus = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.TransactionId = getattr(obj, 'TransactionId', None)
            self.OperationStatus = OperationStatus(getattr(obj, 'OperationStatus', None)) if getattr(obj, 'OperationStatus', None) is not None else None


