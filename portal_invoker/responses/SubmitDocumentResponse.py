

from .BaseApiResponse import BaseApiResponse
from ..objects import SubmitDocumentResultEntity


class SubmitDocumentResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.SubmitDocumentResultEntity = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.SubmitDocumentResultEntity = SubmitDocumentResultEntity(getattr(obj, 'SubmitDocumentResultEntity', None)) if getattr(obj, 'SubmitDocumentResultEntity', None) is not None else None


