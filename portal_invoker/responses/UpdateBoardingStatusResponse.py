

from .BaseApiResponse import BaseApiResponse


class UpdateBoardingStatusResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BoardingInformationId = None
            self.Status = None
            self.StatusCode = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.BoardingInformationId = getattr(obj, 'BoardingInformationId', None)
                self.Status = getattr(obj, 'Status', None)
                self.StatusCode = getattr(obj, 'StatusCode', None)


