




class UpdateSupplierAliasArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.MerchantSupplierId = None
            self.SupplierName = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.MerchantSupplierId = getattr(obj, 'MerchantSupplierId', None)
            self.SupplierName = getattr(obj, 'SupplierName', None)


