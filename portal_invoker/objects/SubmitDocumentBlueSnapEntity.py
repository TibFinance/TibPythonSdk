

from .SubmitDocumentEntity import SubmitDocumentEntity


class SubmitDocumentBlueSnapEntity(SubmitDocumentEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ProviderRequestId = None
            self.CaseId = None
            self.DocType = None
            self.Title = None
            self.FileType = None
            self.Description = None
            self.Content = None

        else:
            super().__init__(obj)

            self.ProviderRequestId = getattr(obj, 'ProviderRequestId', None)
            self.CaseId = getattr(obj, 'CaseId', None)
            self.DocType = getattr(obj, 'DocType', None)
            self.Title = getattr(obj, 'Title', None)
            self.FileType = getattr(obj, 'FileType', None)
            self.Description = getattr(obj, 'Description', None)
            self.Content = getattr(obj, 'Content', None)


