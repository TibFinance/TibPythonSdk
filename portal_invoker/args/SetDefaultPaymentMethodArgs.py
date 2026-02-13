




class SetDefaultPaymentMethodArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.CustomerId = None
            self.PaymentMethodId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.PaymentMethodId = getattr(obj, 'PaymentMethodId', None)


