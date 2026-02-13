




class GetTransactionsByProviderTransactionGroupIdArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.ProviderTransactionGroupId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.ProviderTransactionGroupId = getattr(obj, 'ProviderTransactionGroupId', None)


