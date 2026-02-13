

from .BaseApiResponse import BaseApiResponse


class ApplyChangeValidationResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.RecordIsModify = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.RecordIsModify = getattr(obj, 'RecordIsModify', None)


