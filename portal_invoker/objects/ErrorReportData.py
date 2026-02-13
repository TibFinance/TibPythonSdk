




class ErrorReportData:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Description = None
            self.AccountName = None
            self.MerchantName = None
            self.ErrorDate = None
            self.ErrorDate2 = None
            self.TransactionDate2 = None
            self.CreatedDate = None
            self.ExecutedDate = None
            self.TransactionDate = None
            self.Amount = None
            self.Context = None

        else:
            
            self.Description = getattr(obj, 'Description', None)
            self.AccountName = getattr(obj, 'AccountName', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.ErrorDate = getattr(obj, 'ErrorDate', None)
            self.ErrorDate2 = getattr(obj, 'ErrorDate2', None)
            self.TransactionDate2 = getattr(obj, 'TransactionDate2', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)

            self.ExecutedDate = []
            if hasattr(obj, 'ExecutedDate') and obj.ExecutedDate is not None:
                self.ExecutedDate = [name for name in obj.ExecutedDate]
            self.TransactionDate = getattr(obj, 'TransactionDate', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.Context = getattr(obj, 'Context', None)


