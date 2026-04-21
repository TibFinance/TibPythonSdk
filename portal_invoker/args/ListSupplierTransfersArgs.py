




class ListSupplierTransfersArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.FromDate = None
            self.ToDate = None
            self.OnlyWithErrors = None
            self.MarkResolvedOnly = None
            self.TransferGroupId = None
            self.SupplierMerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.FromDate = getattr(obj, 'FromDate', None)
            self.ToDate = getattr(obj, 'ToDate', None)
            self.OnlyWithErrors = getattr(obj, 'OnlyWithErrors', None)
            self.MarkResolvedOnly = getattr(obj, 'MarkResolvedOnly', None)
            self.TransferGroupId = getattr(obj, 'TransferGroupId', None)
            self.SupplierMerchantId = getattr(obj, 'SupplierMerchantId', None)


