




class GetWalletOperationsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ServiceId = None
            self.From = None
            self.To = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.From = getattr(obj, 'From', None)
            self.To = getattr(obj, 'To', None)


