




class SearchCustomerRelatedPaymentMethod:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PaymentMethodId = None
            self.PaymentMethodDescription = None
            self.PaymentMethodIsDeleted = None
            self.AccountInformationOwner = None

        else:
            
            self.PaymentMethodId = getattr(obj, 'PaymentMethodId', None)
            self.PaymentMethodDescription = getattr(obj, 'PaymentMethodDescription', None)
            self.PaymentMethodIsDeleted = getattr(obj, 'PaymentMethodIsDeleted', None)
            self.AccountInformationOwner = getattr(obj, 'AccountInformationOwner', None)


