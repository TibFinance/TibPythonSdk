




class BaseCreateDirectAccountPaymentMethod:
    def __init__(self, obj=None):
        if obj is None:
            
            self.IsCustomerAutomaticPaymentMethod = None
            self.Token = None
            self.Account = None

        else:
            
            from .Account import Account
            self.IsCustomerAutomaticPaymentMethod = getattr(obj, 'IsCustomerAutomaticPaymentMethod', None)
            self.Token = getattr(obj, 'Token', None)
            self.Account = Account(getattr(obj, 'Account', None)) if getattr(obj, 'Account', None) is not None else None


