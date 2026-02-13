




class ListPaymentMethodsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.CustomerId = None
            self.MerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


