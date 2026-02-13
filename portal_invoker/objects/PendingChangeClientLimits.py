




class PendingChangeClientLimits:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ServiceId = None
            self.ClientWarningDepositLimit = None
            self.ClientWarningCollectionLimit = None

        else:
            
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.ClientWarningDepositLimit = getattr(obj, 'ClientWarningDepositLimit', None)
            self.ClientWarningCollectionLimit = getattr(obj, 'ClientWarningCollectionLimit', None)


