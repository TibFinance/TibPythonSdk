


from ..enums import PaymentFilterLevel


class ListPaymentsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.PaymentFilterLevel = None
            self.LevelFilterId = None
            self.MarkResolvedOnly = None
            self.FromDate = None
            self.ToDate = None
            self.TransferGroupId = None
            self.ExternalMerchantGroupId = None
            self.OnlyWithErrors = None
            self.MerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.PaymentFilterLevel = PaymentFilterLevel(getattr(obj, 'PaymentFilterLevel', None)) if getattr(obj, 'PaymentFilterLevel', None) is not None else None
            self.LevelFilterId = getattr(obj, 'LevelFilterId', None)
            self.MarkResolvedOnly = getattr(obj, 'MarkResolvedOnly', None)
            self.FromDate = getattr(obj, 'FromDate', None)
            self.ToDate = getattr(obj, 'ToDate', None)
            self.TransferGroupId = getattr(obj, 'TransferGroupId', None)
            self.ExternalMerchantGroupId = getattr(obj, 'ExternalMerchantGroupId', None)
            self.OnlyWithErrors = getattr(obj, 'OnlyWithErrors', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


