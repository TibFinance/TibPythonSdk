




class GetMerchantsByExternalIdArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ExternalSystemId = None
            self.ExternalSystemGroupId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ExternalSystemId = getattr(obj, 'ExternalSystemId', None)
            self.ExternalSystemGroupId = getattr(obj, 'ExternalSystemGroupId', None)


