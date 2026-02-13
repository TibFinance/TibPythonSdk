


from ..objects import PendingChangeClientLimits


class ChangeClientWarningLimitRequestArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ClientLimits = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ClientLimits = PendingChangeClientLimits(getattr(obj, 'ClientLimits', None)) if getattr(obj, 'ClientLimits', None) is not None else None


