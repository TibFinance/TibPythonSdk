




class GetUserWhiteLabelingDataArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.Id = None
            self.WhiteLabelingLevel = None
            self.Url = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.Id = getattr(obj, 'Id', None)
            self.WhiteLabelingLevel = getattr(obj, 'WhiteLabelingLevel', None)
            self.Url = getattr(obj, 'Url', None)


