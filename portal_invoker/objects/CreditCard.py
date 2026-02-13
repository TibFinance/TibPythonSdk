




class CreditCard:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CreditCardDescription = None
            self.Pan = None
            self.CVD = None
            self.ExpirationMonth = None
            self.ExpirationYear = None
            self.CardOwner = None
            self.CreditCardRegisteredAddress = None
            self.ExpirationDate = None
            self.FormatedCreditCardString = None
            self.PreviewString = None

        else:
            
            from .Address import Address
            self.CreditCardDescription = getattr(obj, 'CreditCardDescription', None)
            self.Pan = getattr(obj, 'Pan', None)
            self.CVD = getattr(obj, 'CVD', None)
            self.ExpirationMonth = getattr(obj, 'ExpirationMonth', None)
            self.ExpirationYear = getattr(obj, 'ExpirationYear', None)
            self.CardOwner = getattr(obj, 'CardOwner', None)
            self.CreditCardRegisteredAddress = Address(getattr(obj, 'CreditCardRegisteredAddress', None)) if getattr(obj, 'CreditCardRegisteredAddress', None) is not None else None
            self.ExpirationDate = getattr(obj, 'ExpirationDate', None)
            self.FormatedCreditCardString = getattr(obj, 'FormatedCreditCardString', None)
            self.PreviewString = getattr(obj, 'PreviewString', None)


