

from .BaseApiResponse import BaseApiResponse


class SubmitDocumentToBlueSnapResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Status = None
            self.Message = None
            self.Count = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Status = getattr(obj, 'Status', None)
                self.Message = getattr(obj, 'Message', None)
                self.Count = getattr(obj, 'Count', None)


