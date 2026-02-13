




class ClientSettings:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CollectionLimitDaily = None
            self.DepositLimitDaily = None
            self.ClientWarningCollectionLimitDaily = None
            self.ClientWarningDepositLimitDaily = None

        else:
            
            self.CollectionLimitDaily = getattr(obj, 'CollectionLimitDaily', None)
            self.DepositLimitDaily = getattr(obj, 'DepositLimitDaily', None)
            self.ClientWarningCollectionLimitDaily = getattr(obj, 'ClientWarningCollectionLimitDaily', None)
            self.ClientWarningDepositLimitDaily = getattr(obj, 'ClientWarningDepositLimitDaily', None)


