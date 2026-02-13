




class SearchCustomerResult:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CustomerName = None
            self.AccountPreview = None
            self.MerchantName = None
            self.NumberOfTransaction = None
            self.MinTransferAmount = None
            self.MaxTransferAmount = None
            self.MinTransferDueDate = None
            self.MaxTransferDueDate = None

        else:
            
            self.CustomerName = getattr(obj, 'CustomerName', None)
            self.AccountPreview = getattr(obj, 'AccountPreview', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.NumberOfTransaction = getattr(obj, 'NumberOfTransaction', None)
            self.MinTransferAmount = getattr(obj, 'MinTransferAmount', None)
            self.MaxTransferAmount = getattr(obj, 'MaxTransferAmount', None)
            self.MinTransferDueDate = getattr(obj, 'MinTransferDueDate', None)
            self.MaxTransferDueDate = getattr(obj, 'MaxTransferDueDate', None)


