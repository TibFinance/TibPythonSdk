


from ..objects import WhiteLabelingData


class SetWhiteLabelingArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.WhiteLabelingData = None
            self.Id = None
            self.WhiteLabelingLevel = None
            self.Url = None
            self.Logo = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)

            self.WhiteLabelingData = []
            if hasattr(obj, 'WhiteLabelingData') and obj.WhiteLabelingData is not None:
                self.WhiteLabelingData = [WhiteLabelingData(name) for name in  obj.WhiteLabelingData]
            self.Id = getattr(obj, 'Id', None)
            self.WhiteLabelingLevel = getattr(obj, 'WhiteLabelingLevel', None)
            self.Url = getattr(obj, 'Url', None)
            self.Logo = getattr(obj, 'Logo', None)


