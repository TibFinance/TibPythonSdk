




class PayoutPayload:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PayoutId = None
            self.ExternalId = None
            self.Currency = None
            self.PayoutDate = None
            self.TransferCount = None
            self.GrossAmount = None
            self.ProcessingFeesAmount = None
            self.ConvenientFeesAmount = None
            self.NonProcessingFeesAmount = None
            self.TotalPaidAmount = None
            self.CreatedDate = None
            self.Transferts = None

        else:
            
            from .TransferPayload import TransferPayload
            self.PayoutId = getattr(obj, 'PayoutId', None)
            self.ExternalId = getattr(obj, 'ExternalId', None)
            self.Currency = getattr(obj, 'Currency', None)
            self.PayoutDate = getattr(obj, 'PayoutDate', None)
            self.TransferCount = getattr(obj, 'TransferCount', None)
            self.GrossAmount = getattr(obj, 'GrossAmount', None)
            self.ProcessingFeesAmount = getattr(obj, 'ProcessingFeesAmount', None)
            self.ConvenientFeesAmount = getattr(obj, 'ConvenientFeesAmount', None)
            self.NonProcessingFeesAmount = getattr(obj, 'NonProcessingFeesAmount', None)
            self.TotalPaidAmount = getattr(obj, 'TotalPaidAmount', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)

            self.Transferts = []
            if hasattr(obj, 'Transferts') and obj.Transferts is not None:
                self.Transferts = [TransferPayload(name) for name in  obj.Transferts]


