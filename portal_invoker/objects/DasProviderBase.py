


from ..enums import DasProviderType


class DasProviderBase:
    def __init__(self, obj=None):
        if obj is None:
            
            self.DasProviderType = None

        else:
            
            self.DasProviderType = DasProviderType(getattr(obj, 'DasProviderType', None)) if getattr(obj, 'DasProviderType', None) is not None else None


