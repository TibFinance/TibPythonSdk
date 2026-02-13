




class WhiteLabelingData:
    def __init__(self, obj=None):
        if obj is None:
            
            self.WhiteLabelingDataId = None
            self.CssProperty = None
            self.CssValue = None

        else:
            
            self.WhiteLabelingDataId = getattr(obj, 'WhiteLabelingDataId', None)
            self.CssProperty = getattr(obj, 'CssProperty', None)
            self.CssValue = getattr(obj, 'CssValue', None)


