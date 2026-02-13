

from .BillEntity import BillEntity


class BillEntityAdvanced(BillEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.InvoiceNumberPrefix = None
            self.InvoiceNumber = None
            self.PurchaseOrderNumber = None
            self.DueDate = None
            self.InvoiceStatus = None
            self.BillingName = None
            self.BillingEmail = None
            self.BillingPhone = None
            self.BillingAddress1 = None
            self.BillingAddress2 = None
            self.BillingCity = None
            self.BillingProvince = None
            self.BillingPostalCode = None
            self.BillingCountry = None
            self.TaxName1 = None
            self.TaxRate1 = None
            self.TaxNumber1 = None
            self.TaxName2 = None
            self.TaxRate2 = None
            self.TaxNumber2 = None
            self.DiscountPercent = None
            self.DiscountAmount = None
            self.Notes = None
            self.InternalNotes = None
            self.TermsAndConditions = None
            self.FooterText = None
            self.ExternalAccountingId = None
            self.ExternalAccountingSystem = None
            self.Lines = None

        else:
            super().__init__(obj)

            from .BillLineEntity import BillLineEntity
            self.InvoiceNumberPrefix = getattr(obj, 'InvoiceNumberPrefix', None)
            self.InvoiceNumber = getattr(obj, 'InvoiceNumber', None)
            self.PurchaseOrderNumber = getattr(obj, 'PurchaseOrderNumber', None)
            self.DueDate = getattr(obj, 'DueDate', None)
            self.InvoiceStatus = getattr(obj, 'InvoiceStatus', None)
            self.BillingName = getattr(obj, 'BillingName', None)
            self.BillingEmail = getattr(obj, 'BillingEmail', None)
            self.BillingPhone = getattr(obj, 'BillingPhone', None)
            self.BillingAddress1 = getattr(obj, 'BillingAddress1', None)
            self.BillingAddress2 = getattr(obj, 'BillingAddress2', None)
            self.BillingCity = getattr(obj, 'BillingCity', None)
            self.BillingProvince = getattr(obj, 'BillingProvince', None)
            self.BillingPostalCode = getattr(obj, 'BillingPostalCode', None)
            self.BillingCountry = getattr(obj, 'BillingCountry', None)
            self.TaxName1 = getattr(obj, 'TaxName1', None)
            self.TaxRate1 = getattr(obj, 'TaxRate1', None)
            self.TaxNumber1 = getattr(obj, 'TaxNumber1', None)
            self.TaxName2 = getattr(obj, 'TaxName2', None)
            self.TaxRate2 = getattr(obj, 'TaxRate2', None)
            self.TaxNumber2 = getattr(obj, 'TaxNumber2', None)
            self.DiscountPercent = getattr(obj, 'DiscountPercent', None)
            self.DiscountAmount = getattr(obj, 'DiscountAmount', None)
            self.Notes = getattr(obj, 'Notes', None)
            self.InternalNotes = getattr(obj, 'InternalNotes', None)
            self.TermsAndConditions = getattr(obj, 'TermsAndConditions', None)
            self.FooterText = getattr(obj, 'FooterText', None)
            self.ExternalAccountingId = getattr(obj, 'ExternalAccountingId', None)
            self.ExternalAccountingSystem = getattr(obj, 'ExternalAccountingSystem', None)

            self.Lines = []
            if hasattr(obj, 'Lines') and obj.Lines is not None:
                self.Lines = [BillLineEntity(name) for name in  obj.Lines]


