


from ..enums import DasProviderType
from ..objects import DasProviderEntityQuebec
from ..objects import DasProviderEntityCanada


class AddNewDasProviderArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.DasProviderType = None
            self.DasProviderQuebec = None
            self.DasProviderCanada = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.DasProviderType = DasProviderType(getattr(obj, 'DasProviderType', None)) if getattr(obj, 'DasProviderType', None) is not None else None
            self.DasProviderQuebec = DasProviderEntityQuebec(getattr(obj, 'DasProviderQuebec', None)) if getattr(obj, 'DasProviderQuebec', None) is not None else None
            self.DasProviderCanada = DasProviderEntityCanada(getattr(obj, 'DasProviderCanada', None)) if getattr(obj, 'DasProviderCanada', None) is not None else None


