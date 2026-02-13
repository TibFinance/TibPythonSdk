




class ProcessDropInWhitExistingPaymentMethodIdArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.PaymentMethodId = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.PaymentMethodId = getattr(obj, 'PaymentMethodId', None)


