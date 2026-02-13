

from .BoardingBaseResult import BoardingBaseResult


class RetrieveDocumentResultEntity(BoardingBaseResult):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CaseStatus = None
            self.ProviderRequestId = None
            self.CaseId = None
            self.Documentation = None

        else:
            super().__init__(obj)

            from .BoardingDocument import BoardingDocument
            self.CaseStatus = getattr(obj, 'CaseStatus', None)
            self.ProviderRequestId = getattr(obj, 'ProviderRequestId', None)
            self.CaseId = getattr(obj, 'CaseId', None)

            self.Documentation = []
            if hasattr(obj, 'Documentation') and obj.Documentation is not None:
                self.Documentation = [BoardingDocument(name) for name in  obj.Documentation]


