


from ..enums import Provider


class SetMerchantProviderArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.MerchantId = None
            self.FavoriteProvider = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.FavoriteProvider = Provider(getattr(obj, 'FavoriteProvider', None)) if getattr(obj, 'FavoriteProvider', None) is not None else None


