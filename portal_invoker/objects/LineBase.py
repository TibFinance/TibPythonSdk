

from .FlatFileLine import FlatFileLine
from ..enums import PadDirection


class LineBase(FlatFileLine):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.DefaultPaddingChar = None
            self.DefaultPaddingDirection = None

        else:
            super().__init__(obj)

            self.DefaultPaddingChar = getattr(obj, 'DefaultPaddingChar', None)
            self.DefaultPaddingDirection = PadDirection(getattr(obj, 'DefaultPaddingDirection', None)) if getattr(obj, 'DefaultPaddingDirection', None) is not None else None


