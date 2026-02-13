


from ..objects import BoardingEntity
from ..objects import TransactionMailingInfo
from ..objects import ProviderAccount


class BoardingArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.BoardingEntity = None
            self.MailingInfo = None
            self.ProviderCredentials = None

        else:
            
            self.BoardingEntity = BoardingEntity(getattr(obj, 'BoardingEntity', None)) if getattr(obj, 'BoardingEntity', None) is not None else None
            self.MailingInfo = TransactionMailingInfo(getattr(obj, 'MailingInfo', None)) if getattr(obj, 'MailingInfo', None) is not None else None

            self.ProviderCredentials = []
            if hasattr(obj, 'ProviderCredentials') and obj.ProviderCredentials is not None:
                self.ProviderCredentials = [ProviderAccount(name) for name in  obj.ProviderCredentials]


