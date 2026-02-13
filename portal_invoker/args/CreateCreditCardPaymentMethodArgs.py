


from ..enums import Currency
from ..objects import CreditCard
from ..enums import Language


class CreateCreditCardPaymentMethodArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.Currency = None
            self.CustomerId = None
            self.IsCustomerAutomaticPaymentMethod = None
            self.CreditCard = None
            self.CardOwner = None
            self.ZipCode = None
            self.Language = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.IsCustomerAutomaticPaymentMethod = getattr(obj, 'IsCustomerAutomaticPaymentMethod', None)
            self.CreditCard = CreditCard(getattr(obj, 'CreditCard', None)) if getattr(obj, 'CreditCard', None) is not None else None
            self.CardOwner = getattr(obj, 'CardOwner', None)
            self.ZipCode = getattr(obj, 'ZipCode', None)
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None


