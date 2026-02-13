

from .BaseApiResponse import BaseApiResponse


class CreateBoardingDocumentsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Status = None
            self.Message = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Status = getattr(obj, 'Status', None)
                self.Message = getattr(obj, 'Message', None)


