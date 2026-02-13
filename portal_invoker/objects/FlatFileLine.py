


from ..enums import PadDirection


class FlatFileLine:
    def __init__(self, obj=None):
        if obj is None:
            
            self.DefaultPaddingChar = None
            self.DefaultPaddingDirection = None
            self.StartPosition = None

        else:
            
            self.DefaultPaddingChar = getattr(obj, 'DefaultPaddingChar', None)
            self.DefaultPaddingDirection = PadDirection(getattr(obj, 'DefaultPaddingDirection', None)) if getattr(obj, 'DefaultPaddingDirection', None) is not None else None
            self.StartPosition = getattr(obj, 'StartPosition', None)


