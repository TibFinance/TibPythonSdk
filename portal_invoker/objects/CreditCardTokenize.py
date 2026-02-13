




class CreditCardTokenize:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CardToken = None
            self.IsValid = None
            self.ErrorMessage = None

        else:
            
            self.CardToken = getattr(obj, 'CardToken', None)
            self.IsValid = getattr(obj, 'IsValid', None)
            self.ErrorMessage = getattr(obj, 'ErrorMessage', None)


