


from ..objects import ClientEntity
from ..objects import ClientLogin
from ..objects import ServiceEntity
from ..objects import Merchant
from ..objects import ServiceFeeSettings
from ..objects import ServiceSettings
from ..objects import ClientSettings


class CreateClientNewAdminArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.Client = None
            self.Password = None
            self.ClientLogin = None
            self.ServiceInfo = None
            self.CreateInnactive = None
            self.MerchantInfo = None
            self.ServiceFeeSettings = None
            self.Settings = None
            self.ClientSettings = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.Client = ClientEntity(getattr(obj, 'Client', None)) if getattr(obj, 'Client', None) is not None else None
            self.Password = getattr(obj, 'Password', None)
            self.ClientLogin = ClientLogin(getattr(obj, 'ClientLogin', None)) if getattr(obj, 'ClientLogin', None) is not None else None
            self.ServiceInfo = ServiceEntity(getattr(obj, 'ServiceInfo', None)) if getattr(obj, 'ServiceInfo', None) is not None else None
            self.CreateInnactive = getattr(obj, 'CreateInnactive', None)
            self.MerchantInfo = Merchant(getattr(obj, 'MerchantInfo', None)) if getattr(obj, 'MerchantInfo', None) is not None else None
            self.ServiceFeeSettings = ServiceFeeSettings(getattr(obj, 'ServiceFeeSettings', None)) if getattr(obj, 'ServiceFeeSettings', None) is not None else None
            self.Settings = ServiceSettings(getattr(obj, 'Settings', None)) if getattr(obj, 'Settings', None) is not None else None
            self.ClientSettings = ClientSettings(getattr(obj, 'ClientSettings', None)) if getattr(obj, 'ClientSettings', None) is not None else None


