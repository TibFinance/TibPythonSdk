




class ResendPaymentEmailArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.PaymentId = None
            self.MerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.PaymentId = getattr(obj, 'PaymentId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


