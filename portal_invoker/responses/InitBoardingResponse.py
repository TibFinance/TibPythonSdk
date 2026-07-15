

from .BaseApiResponse import BaseApiResponse


class InitBoardingResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.RedirectUrl = None

        else:
            super().__init__(obj)
            self.RedirectUrl = getattr(obj, 'RedirectUrl', None)


