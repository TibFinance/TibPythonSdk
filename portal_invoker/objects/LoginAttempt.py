


from ..enums import UserType


class LoginAttempt:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Type = None
            self.Attempts = None

        else:
            
            self.Type = UserType(getattr(obj, 'Type', None)) if getattr(obj, 'Type', None) is not None else None

            self.Attempts = []
            if hasattr(obj, 'Attempts') and obj.Attempts is not None:
                self.Attempts = [name for name in obj.Attempts]


