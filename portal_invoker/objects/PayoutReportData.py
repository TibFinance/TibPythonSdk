


from ..enums import Currency


class PayoutReportData:
    def __init__(self, obj=None):
        if obj is None:
            
            self.TransferCount = None
            self.ExternalId = None
            self.Currency = None
            self.PayoutDate = None
            self.GrossAmount = None
            self.ProcessingFeesAmount = None
            self.ConvenientFeesAmount = None
            self.NonProcessingFeesAmount = None
            self.TotalPaidAmount = None
            self.RefundsAmount = None
            self.NonProcessingDescriptions = None

        else:
            
            self.TransferCount = getattr(obj, 'TransferCount', None)
            self.ExternalId = getattr(obj, 'ExternalId', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.PayoutDate = getattr(obj, 'PayoutDate', None)
            self.GrossAmount = getattr(obj, 'GrossAmount', None)
            self.ProcessingFeesAmount = getattr(obj, 'ProcessingFeesAmount', None)
            self.ConvenientFeesAmount = getattr(obj, 'ConvenientFeesAmount', None)
            self.NonProcessingFeesAmount = getattr(obj, 'NonProcessingFeesAmount', None)
            self.TotalPaidAmount = getattr(obj, 'TotalPaidAmount', None)
            self.RefundsAmount = getattr(obj, 'RefundsAmount', None)

            self.NonProcessingDescriptions = []
            if hasattr(obj, 'NonProcessingDescriptions') and obj.NonProcessingDescriptions is not None:
                self.NonProcessingDescriptions = [name for name in obj.NonProcessingDescriptions]


