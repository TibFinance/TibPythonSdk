


from ..objects import ContactInfo


class SaveCustomerContactInfoArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.CustomerId = None
            self.ContactInfo = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.ContactInfo = ContactInfo(getattr(obj, 'ContactInfo', None)) if getattr(obj, 'ContactInfo', None) is not None else None


