

from .BaseApiResponse import BaseApiResponse
from ..objects import RetrieveDocumentResultEntity


class RetrieveDocumentResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.RetrieveDocumentResultEntity = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.RetrieveDocumentResultEntity = RetrieveDocumentResultEntity(getattr(obj, 'RetrieveDocumentResultEntity', None)) if getattr(obj, 'RetrieveDocumentResultEntity', None) is not None else None


