


from ..objects import SubmitDocumentEntity
from ..objects import TransactionMailingInfo
from ..objects import ProviderAccount


class SubmitDocumentArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SubmitDocumentEntity = None
            self.MailingInfo = None
            self.ProviderCredentials = None

        else:
            
            self.SubmitDocumentEntity = SubmitDocumentEntity(getattr(obj, 'SubmitDocumentEntity', None)) if getattr(obj, 'SubmitDocumentEntity', None) is not None else None
            self.MailingInfo = TransactionMailingInfo(getattr(obj, 'MailingInfo', None)) if getattr(obj, 'MailingInfo', None) is not None else None

            self.ProviderCredentials = []
            if hasattr(obj, 'ProviderCredentials') and obj.ProviderCredentials is not None:
                self.ProviderCredentials = [ProviderAccount(name) for name in  obj.ProviderCredentials]


