


from ..objects import Account


class ProcessDropInDirectAccountArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.IsPPAAuthorized = None
            self.Account = None

        else:
            
            self.IsPPAAuthorized = getattr(obj, 'IsPPAAuthorized', None)
            self.Account = Account(getattr(obj, 'Account', None)) if getattr(obj, 'Account', None) is not None else None


