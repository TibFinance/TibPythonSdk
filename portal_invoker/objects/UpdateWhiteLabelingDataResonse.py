




class UpdateWhiteLabelingDataResonse:
    def __init__(self, obj=None):
        if obj is None:
            
            self.WhiteLabeling = None

        else:
            
            from .WhiteLabeling import WhiteLabeling
            self.WhiteLabeling = WhiteLabeling(getattr(obj, 'WhiteLabeling', None)) if getattr(obj, 'WhiteLabeling', None) is not None else None


