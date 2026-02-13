


from ..enums import PadDirection


class FlatFileEntry:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Position = None
            self.Length = None
            self.PadChar = None
            self.PadDirection = None
            self.Value = None
            self.ValueString = None

        else:
            
            self.Position = getattr(obj, 'Position', None)
            self.Length = getattr(obj, 'Length', None)
            self.PadChar = getattr(obj, 'PadChar', None)
            self.PadDirection = PadDirection(getattr(obj, 'PadDirection', None)) if getattr(obj, 'PadDirection', None) is not None else None
            self.Value = getattr(obj, 'Value', None)
            self.ValueString = getattr(obj, 'ValueString', None)


