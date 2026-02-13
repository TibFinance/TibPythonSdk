




class DuplicateOperationArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.OperationId = None
            self.TransferId = None
            self.Amount = None
            self.OperationTarget = None
            self.OperationDirection = None
            self.DependentOperationId = None
            self.OperationStatus = None
            self.TransactionGroupId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.OperationId = getattr(obj, 'OperationId', None)
            self.TransferId = getattr(obj, 'TransferId', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.OperationTarget = getattr(obj, 'OperationTarget', None)
            self.OperationDirection = getattr(obj, 'OperationDirection', None)
            self.DependentOperationId = getattr(obj, 'DependentOperationId', None)
            self.OperationStatus = getattr(obj, 'OperationStatus', None)
            self.TransactionGroupId = getattr(obj, 'TransactionGroupId', None)


