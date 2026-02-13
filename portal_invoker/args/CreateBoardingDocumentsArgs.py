




class CreateBoardingDocumentsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.CaseId = None
            self.DocType = None
            self.Filename = None
            self.Description = None
            self.Content = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.CaseId = getattr(obj, 'CaseId', None)
            self.DocType = getattr(obj, 'DocType', None)
            self.Filename = getattr(obj, 'Filename', None)
            self.Description = getattr(obj, 'Description', None)
            self.Content = getattr(obj, 'Content', None)


