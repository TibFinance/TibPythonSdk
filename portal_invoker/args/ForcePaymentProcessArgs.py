




class ForcePaymentProcessArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.IdempotencyKey = None
            self.PaymentId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.IdempotencyKey = getattr(obj, 'IdempotencyKey', None)
            self.PaymentId = getattr(obj, 'PaymentId', None)


