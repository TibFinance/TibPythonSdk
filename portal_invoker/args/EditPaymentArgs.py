




class EditPaymentArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.PaymentId = None
            self.MerchantId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.PaymentId = getattr(obj, 'PaymentId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


