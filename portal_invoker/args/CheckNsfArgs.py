


from ..objects import Account


class CheckNsfArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ServiceId = None
            self.Account = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.Account = Account(getattr(obj, 'Account', None)) if getattr(obj, 'Account', None) is not None else None


