


from ..enums import Provider


class AddProviderTransactionsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.Provider = None
            self.FileContent = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.Provider = Provider(getattr(obj, 'Provider', None)) if getattr(obj, 'Provider', None) is not None else None
            self.FileContent = getattr(obj, 'FileContent', None)


