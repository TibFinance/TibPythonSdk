




class BatchFileEventOperation:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Success = None
            self.CreatedTransferId = None
            self.Amount = None
            self.ClientId = None
            self.CustomerId = None
            self.MerchantId = None
            self.ReferenceId = None
            self.PaymentMethodId = None

        else:
            
            self.Success = getattr(obj, 'Success', None)
            self.CreatedTransferId = getattr(obj, 'CreatedTransferId', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.ReferenceId = getattr(obj, 'ReferenceId', None)
            self.PaymentMethodId = getattr(obj, 'PaymentMethodId', None)


