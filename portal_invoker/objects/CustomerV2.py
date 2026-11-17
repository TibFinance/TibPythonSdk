
from ..utility import to_enum

from ..enums import Language


class CustomerV2:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CustomerName = None
            self.CustomerExternalId = None
            self.Language = None
            self.CustomerDescription = None
            self.ContactInfo = None

        else:
            
            from .ContactInfo import ContactInfo
            self.CustomerName = getattr(obj, 'CustomerName', None)
            self.CustomerExternalId = getattr(obj, 'CustomerExternalId', None)
            self.Language = to_enum(Language, getattr(obj, 'Language', None))
            self.CustomerDescription = getattr(obj, 'CustomerDescription', None)
            self.ContactInfo = ContactInfo(getattr(obj, 'ContactInfo', None)) if getattr(obj, 'ContactInfo', None) is not None else None


