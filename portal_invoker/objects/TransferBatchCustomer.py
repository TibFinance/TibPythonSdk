
from ..utility import to_enum

from ..enums import Language


class TransferBatchCustomer:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CustomerId = None
            self.CustomerExternalId = None
            self.CustomerName = None
            self.Language = None
            self.ContactInfo = None

        else:
            
            from .ContactInfo import ContactInfo
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.CustomerExternalId = getattr(obj, 'CustomerExternalId', None)
            self.CustomerName = getattr(obj, 'CustomerName', None)
            self.Language = to_enum(Language, getattr(obj, 'Language', None))
            self.ContactInfo = ContactInfo(getattr(obj, 'ContactInfo', None)) if getattr(obj, 'ContactInfo', None) is not None else None


