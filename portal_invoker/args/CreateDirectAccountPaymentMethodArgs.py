


from ..objects import Account
from ..enums import Language


class CreateDirectAccountPaymentMethodArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.CustomerId = None
            self.IsCustomerAutomaticPaymentMethod = None
            self.Account = None
            self.Language = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.IsCustomerAutomaticPaymentMethod = getattr(obj, 'IsCustomerAutomaticPaymentMethod', None)
            self.Account = Account(getattr(obj, 'Account', None)) if getattr(obj, 'Account', None) is not None else None
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None


