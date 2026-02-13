

from .BaseApiResponse import BaseApiResponse
from ..objects import BillLineEntity


class CreateBillAdvancedResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BillId = None
            self.InvoiceNumber = None
            self.FullInvoiceNumber = None
            self.Subtotal = None
            self.DiscountTotal = None
            self.TaxAmount1 = None
            self.TaxAmount2 = None
            self.TotalAmount = None
            self.Lines = None
            self.PaymentUrl = None
            self.PdfUrl = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.BillId = getattr(obj, 'BillId', None)
                self.InvoiceNumber = getattr(obj, 'InvoiceNumber', None)
                self.FullInvoiceNumber = getattr(obj, 'FullInvoiceNumber', None)
                self.Subtotal = getattr(obj, 'Subtotal', None)
                self.DiscountTotal = getattr(obj, 'DiscountTotal', None)
                self.TaxAmount1 = getattr(obj, 'TaxAmount1', None)
                self.TaxAmount2 = getattr(obj, 'TaxAmount2', None)
                self.TotalAmount = getattr(obj, 'TotalAmount', None)

                self.Lines = []
                if hasattr(obj, 'Lines') and obj.Lines is not None:
                    self.Lines = [BillLineEntity(name) for name in  obj.Lines]
                self.PaymentUrl = getattr(obj, 'PaymentUrl', None)
                self.PdfUrl = getattr(obj, 'PdfUrl', None)


