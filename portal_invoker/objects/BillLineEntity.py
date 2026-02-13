




class BillLineEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.BillLineId = None
            self.LineNumber = None
            self.ProductSku = None
            self.ProductName = None
            self.ProductDescription = None
            self.Quantity = None
            self.UnitOfMeasure = None
            self.UnitPrice = None
            self.DiscountPercent = None
            self.DiscountAmount = None
            self.TaxCode = None
            self.IsTaxable = None
            self.LineSubtotal = None
            self.LineTaxAmount = None
            self.LineTotal = None

        else:
            
            self.BillLineId = getattr(obj, 'BillLineId', None)
            self.LineNumber = getattr(obj, 'LineNumber', None)
            self.ProductSku = getattr(obj, 'ProductSku', None)
            self.ProductName = getattr(obj, 'ProductName', None)
            self.ProductDescription = getattr(obj, 'ProductDescription', None)
            self.Quantity = getattr(obj, 'Quantity', None)
            self.UnitOfMeasure = getattr(obj, 'UnitOfMeasure', None)
            self.UnitPrice = getattr(obj, 'UnitPrice', None)
            self.DiscountPercent = getattr(obj, 'DiscountPercent', None)
            self.DiscountAmount = getattr(obj, 'DiscountAmount', None)
            self.TaxCode = getattr(obj, 'TaxCode', None)
            self.IsTaxable = getattr(obj, 'IsTaxable', None)
            self.LineSubtotal = getattr(obj, 'LineSubtotal', None)
            self.LineTaxAmount = getattr(obj, 'LineTaxAmount', None)
            self.LineTotal = getattr(obj, 'LineTotal', None)


