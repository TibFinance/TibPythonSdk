


from ..objects import WhiteLabelingData


class SetDefaultWhiteLabelingArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.WhiteLabelingData = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)

            self.WhiteLabelingData = []
            if hasattr(obj, 'WhiteLabelingData') and obj.WhiteLabelingData is not None:
                self.WhiteLabelingData = [WhiteLabelingData(name) for name in  obj.WhiteLabelingData]


