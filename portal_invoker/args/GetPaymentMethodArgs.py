




class GetPaymentMethodArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.PaymentMethodId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.PaymentMethodId = getattr(obj, 'PaymentMethodId', None)


