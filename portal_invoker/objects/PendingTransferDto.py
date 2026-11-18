




class PendingTransferDto:
    def __init__(self, obj=None):
        if obj is None:
            
            self.TransferId = None
            self.Amount = None
            self.Direction = None
            self.CustomerName = None
            self.CreatedDate = None
            self.ServiceId = None
            self.ServiceName = None

        else:
            
            self.TransferId = getattr(obj, 'TransferId', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.Direction = getattr(obj, 'Direction', None)
            self.CustomerName = getattr(obj, 'CustomerName', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.ServiceName = getattr(obj, 'ServiceName', None)


