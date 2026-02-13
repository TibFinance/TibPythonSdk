


from ..objects import CreditCard


class ProcessDropInCreditCardArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.IsPPAAuthorized = None
            self.CreditCard = None

        else:
            
            self.IsPPAAuthorized = getattr(obj, 'IsPPAAuthorized', None)
            self.CreditCard = CreditCard(getattr(obj, 'CreditCard', None)) if getattr(obj, 'CreditCard', None) is not None else None


