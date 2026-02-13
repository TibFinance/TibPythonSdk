

from .RetrieveDocumentEntity import RetrieveDocumentEntity


class RetrieveDocumentBlueSnapEntity(RetrieveDocumentEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ProviderRequestId = None
            self.CaseId = None

        else:
            super().__init__(obj)

            self.ProviderRequestId = getattr(obj, 'ProviderRequestId', None)
            self.CaseId = getattr(obj, 'CaseId', None)


