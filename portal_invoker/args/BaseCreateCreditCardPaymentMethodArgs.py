


from ..objects import CreditCard


class BaseCreateCreditCardPaymentMethodArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.IsCustomerAutomaticPaymentMethod = None
            self.CreditCard = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.IsCustomerAutomaticPaymentMethod = getattr(obj, 'IsCustomerAutomaticPaymentMethod', None)
            self.CreditCard = CreditCard(getattr(obj, 'CreditCard', None)) if getattr(obj, 'CreditCard', None) is not None else None


