


from ..enums import Provider


class ProviderEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ProviderId = None
            self.ProviderType = None
            self.OrderPriority = None

        else:
            
            self.ProviderId = getattr(obj, 'ProviderId', None)
            self.ProviderType = Provider(getattr(obj, 'ProviderType', None)) if getattr(obj, 'ProviderType', None) is not None else None
            self.OrderPriority = getattr(obj, 'OrderPriority', None)


