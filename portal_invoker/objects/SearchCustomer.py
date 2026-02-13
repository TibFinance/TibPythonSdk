




class SearchCustomer:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ClientId = None
            self.ClientName = None
            self.ClientIsDeleted = None
            self.ServiceId = None
            self.ServiceName = None
            self.ServiceIsDeleted = None
            self.FoundUpMerchants = None
            self.RelatedPaymentMethods = None
            self.CustomerId = None
            self.CustomerName = None
            self.IsCustomerDeleted = None

        else:
            
            from .SearchCustomerRelatedMerchant import SearchCustomerRelatedMerchant
            from .SearchCustomerRelatedPaymentMethod import SearchCustomerRelatedPaymentMethod
            self.ClientId = getattr(obj, 'ClientId', None)
            self.ClientName = getattr(obj, 'ClientName', None)
            self.ClientIsDeleted = getattr(obj, 'ClientIsDeleted', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.ServiceName = getattr(obj, 'ServiceName', None)
            self.ServiceIsDeleted = getattr(obj, 'ServiceIsDeleted', None)

            self.FoundUpMerchants = []
            if hasattr(obj, 'FoundUpMerchants') and obj.FoundUpMerchants is not None:
                self.FoundUpMerchants = [SearchCustomerRelatedMerchant(name) for name in  obj.FoundUpMerchants]

            self.RelatedPaymentMethods = []
            if hasattr(obj, 'RelatedPaymentMethods') and obj.RelatedPaymentMethods is not None:
                self.RelatedPaymentMethods = [SearchCustomerRelatedPaymentMethod(name) for name in  obj.RelatedPaymentMethods]
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.CustomerName = getattr(obj, 'CustomerName', None)
            self.IsCustomerDeleted = getattr(obj, 'IsCustomerDeleted', None)


