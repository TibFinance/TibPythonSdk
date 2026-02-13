




class DeleteMerchantLoginArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.LoginsUserRelationsId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.LoginsUserRelationsId = getattr(obj, 'LoginsUserRelationsId', None)


