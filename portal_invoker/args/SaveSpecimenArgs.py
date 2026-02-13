


from ..objects import Account


class SaveSpecimenArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.ClientId = None
            self.Account = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.Account = Account(getattr(obj, 'Account', None)) if getattr(obj, 'Account', None) is not None else None


