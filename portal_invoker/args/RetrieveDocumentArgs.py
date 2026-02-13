


from ..objects import RetrieveDocumentEntity
from ..objects import TransactionMailingInfo
from ..objects import ProviderAccount


class RetrieveDocumentArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.RetrieveDocumentEntity = None
            self.MailingInfo = None
            self.ProviderCredentials = None

        else:
            
            self.RetrieveDocumentEntity = RetrieveDocumentEntity(getattr(obj, 'RetrieveDocumentEntity', None)) if getattr(obj, 'RetrieveDocumentEntity', None) is not None else None
            self.MailingInfo = TransactionMailingInfo(getattr(obj, 'MailingInfo', None)) if getattr(obj, 'MailingInfo', None) is not None else None

            self.ProviderCredentials = []
            if hasattr(obj, 'ProviderCredentials') and obj.ProviderCredentials is not None:
                self.ProviderCredentials = [ProviderAccount(name) for name in  obj.ProviderCredentials]


