


from ..enums import Provider


class ProviderAccountOperations:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ProviderType = None
            self.AccountOperations = None

        else:
            
            from .AccountOperationLine import AccountOperationLine
            self.ProviderType = Provider(getattr(obj, 'ProviderType', None)) if getattr(obj, 'ProviderType', None) is not None else None

            self.AccountOperations = []
            if hasattr(obj, 'AccountOperations') and obj.AccountOperations is not None:
                self.AccountOperations = [AccountOperationLine(name) for name in  obj.AccountOperations]


