


from ..enums import AccountOperationDirection


class AccountOperationLine:
    def __init__(self, obj=None):
        if obj is None:
            
            self.OperationDate = None
            self.OperationDescription = None
            self.Amount = None
            self.AccountOperationDirection = None

        else:
            
            self.OperationDate = getattr(obj, 'OperationDate', None)
            self.OperationDescription = getattr(obj, 'OperationDescription', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.AccountOperationDirection = AccountOperationDirection(getattr(obj, 'AccountOperationDirection', None)) if getattr(obj, 'AccountOperationDirection', None) is not None else None


