




class DeleteWhiteLabelingArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.Id = None
            self.Level = None
            self.Url = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.Id = getattr(obj, 'Id', None)
            self.Level = getattr(obj, 'Level', None)
            self.Url = getattr(obj, 'Url', None)


