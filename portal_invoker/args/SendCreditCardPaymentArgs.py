


from ..objects import CreditCard


class SendCreditCardPaymentArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PaymentId = None
            self.CreditCard = None
            self.PaymentAmount = None

        else:
            
            self.PaymentId = getattr(obj, 'PaymentId', None)
            self.CreditCard = CreditCard(getattr(obj, 'CreditCard', None)) if getattr(obj, 'CreditCard', None) is not None else None
            self.PaymentAmount = getattr(obj, 'PaymentAmount', None)


