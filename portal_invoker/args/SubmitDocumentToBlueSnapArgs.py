




class SubmitDocumentToBlueSnapArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ProviderRequestId = None
            self.DocType = None
            self.Title = None
            self.FileType = None
            self.Description = None
            self.Content = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ProviderRequestId = getattr(obj, 'ProviderRequestId', None)
            self.DocType = getattr(obj, 'DocType', None)
            self.Title = getattr(obj, 'Title', None)
            self.FileType = getattr(obj, 'FileType', None)
            self.Description = getattr(obj, 'Description', None)
            self.Content = getattr(obj, 'Content', None)


