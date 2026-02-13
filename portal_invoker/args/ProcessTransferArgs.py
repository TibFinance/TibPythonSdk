


from ..objects import ProcessTransferEntity
from ..objects import TransactionMailingInfo
from ..objects import ProviderAccount


class ProcessTransferArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.TransferInformations = None
            self.MailingInfo = None
            self.ProviderCredentials = None

        else:
            

            self.TransferInformations = []
            if hasattr(obj, 'TransferInformations') and obj.TransferInformations is not None:
                self.TransferInformations = [ProcessTransferEntity(name) for name in  obj.TransferInformations]
            self.MailingInfo = TransactionMailingInfo(getattr(obj, 'MailingInfo', None)) if getattr(obj, 'MailingInfo', None) is not None else None

            self.ProviderCredentials = []
            if hasattr(obj, 'ProviderCredentials') and obj.ProviderCredentials is not None:
                self.ProviderCredentials = [ProviderAccount(name) for name in  obj.ProviderCredentials]


