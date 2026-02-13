




class DeletePaymentMethodBulkArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.PaymentMethodIds = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)

            self.PaymentMethodIds = []
            if hasattr(obj, 'PaymentMethodIds') and obj.PaymentMethodIds is not None:
                self.PaymentMethodIds = [name for name in obj.PaymentMethodIds]


