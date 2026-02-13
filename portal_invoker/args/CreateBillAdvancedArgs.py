


from ..objects import BillEntityAdvanced


class CreateBillAdvancedArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.BillData = None
            self.BreakIfMerchantNeverBeenAuthorized = None
            self.AutoCalculateTotals = None
            self.AutoGenerateInvoiceNumber = None
            self.SendEmailOnCreate = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.BillData = BillEntityAdvanced(getattr(obj, 'BillData', None)) if getattr(obj, 'BillData', None) is not None else None
            self.BreakIfMerchantNeverBeenAuthorized = getattr(obj, 'BreakIfMerchantNeverBeenAuthorized', None)
            self.AutoCalculateTotals = getattr(obj, 'AutoCalculateTotals', None)
            self.AutoGenerateInvoiceNumber = getattr(obj, 'AutoGenerateInvoiceNumber', None)
            self.SendEmailOnCreate = getattr(obj, 'SendEmailOnCreate', None)


