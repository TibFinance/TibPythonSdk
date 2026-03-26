




class SupplierView:
    def __init__(self, obj=None):
        if obj is None:
            
            self.MerchantSupplierId = None
            self.SupplierId = None
            self.SupplierName = None
            self.SupplierEmail = None
            self.Created = None

        else:
            
            self.MerchantSupplierId = getattr(obj, 'MerchantSupplierId', None)
            self.SupplierId = getattr(obj, 'SupplierId', None)
            self.SupplierName = getattr(obj, 'SupplierName', None)
            self.SupplierEmail = getattr(obj, 'SupplierEmail', None)
            self.Created = getattr(obj, 'Created', None)


