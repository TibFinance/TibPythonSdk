




class ProviderAddressEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.UrlType = None
            self.Url = None
            self.Port = None

        else:
            
            self.UrlType = getattr(obj, 'UrlType', None)
            self.Url = getattr(obj, 'Url', None)
            self.Port = getattr(obj, 'Port', None)


