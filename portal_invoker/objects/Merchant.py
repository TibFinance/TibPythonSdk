




class Merchant:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Account = None

        else:
            
            from .Account import Account
            self.Account = Account(getattr(obj, 'Account', None)) if getattr(obj, 'Account', None) is not None else None


