
from ..utility import to_enum

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
            self.Language = to_enum(Language, getattr(obj, 'Language', None))
            self.Currency = to_enum(Currency, getattr(obj, 'Currency', None))


