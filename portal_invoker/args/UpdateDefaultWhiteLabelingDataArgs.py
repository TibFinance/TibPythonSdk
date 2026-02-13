


from ..objects import WhiteLabelingData


class UpdateDefaultWhiteLabelingDataArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.UpdatedWhiteLabelingData = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)

            self.UpdatedWhiteLabelingData = []
            if hasattr(obj, 'UpdatedWhiteLabelingData') and obj.UpdatedWhiteLabelingData is not None:
                self.UpdatedWhiteLabelingData = [WhiteLabelingData(name) for name in  obj.UpdatedWhiteLabelingData]


