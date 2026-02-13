




class DeletePaymentBulkArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.PaymentIds = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)

            self.PaymentIds = []
            if hasattr(obj, 'PaymentIds') and obj.PaymentIds is not None:
                self.PaymentIds = [name for name in obj.PaymentIds]


