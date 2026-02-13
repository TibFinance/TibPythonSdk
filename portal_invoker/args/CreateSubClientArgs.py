


from ..enums import Language
from ..enums import Currency


class CreateSubClientArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.Name = None
            self.Language = None
            self.Currency = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.Name = getattr(obj, 'Name', None)
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None


