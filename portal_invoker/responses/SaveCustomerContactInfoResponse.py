

from .BaseApiResponse import BaseApiResponse
from ..objects import ContactInfo


class SaveCustomerContactInfoResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ContactInfo = None

        else:
            super().__init__(obj)
            self.ContactInfo = ContactInfo(getattr(obj, 'ContactInfo', None)) if getattr(obj, 'ContactInfo', None) is not None else None


