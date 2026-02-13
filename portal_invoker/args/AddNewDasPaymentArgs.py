


from ..enums import DasProviderType
from ..objects import DasPaymentCanadaEntity
from ..objects import DasPaymentQuebecEntity


class AddNewDasPaymentArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.DasProviderId = None
            self.DasPaymentProviderType = None
            self.DasPaymentCanada = None
            self.DasPaymentQuebec = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.DasProviderId = getattr(obj, 'DasProviderId', None)
            self.DasPaymentProviderType = DasProviderType(getattr(obj, 'DasPaymentProviderType', None)) if getattr(obj, 'DasPaymentProviderType', None) is not None else None
            self.DasPaymentCanada = DasPaymentCanadaEntity(getattr(obj, 'DasPaymentCanada', None)) if getattr(obj, 'DasPaymentCanada', None) is not None else None
            self.DasPaymentQuebec = DasPaymentQuebecEntity(getattr(obj, 'DasPaymentQuebec', None)) if getattr(obj, 'DasPaymentQuebec', None) is not None else None


