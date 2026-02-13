




class WhiteLabeling:
    def __init__(self, obj=None):
        if obj is None:
            
            self.WhileLabelingId = None
            self.WhiteLabelingLevel = None
            self.WhiteLabelingLevelValue = None
            self.Logo = None
            self.Url = None
            self.WhiteLabelingData = None

        else:
            
            from .WhiteLabelingData import WhiteLabelingData
            self.WhileLabelingId = getattr(obj, 'WhileLabelingId', None)
            self.WhiteLabelingLevel = getattr(obj, 'WhiteLabelingLevel', None)
            self.WhiteLabelingLevelValue = getattr(obj, 'WhiteLabelingLevelValue', None)
            self.Logo = getattr(obj, 'Logo', None)
            self.Url = getattr(obj, 'Url', None)

            self.WhiteLabelingData = []
            if hasattr(obj, 'WhiteLabelingData') and obj.WhiteLabelingData is not None:
                self.WhiteLabelingData = [WhiteLabelingData(name) for name in  obj.WhiteLabelingData]


