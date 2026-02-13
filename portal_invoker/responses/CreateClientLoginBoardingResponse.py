

from .BaseApiResponse import BaseApiResponse


class CreateClientLoginBoardingResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.RedirectUrl = None
            self.Token = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.RedirectUrl = getattr(obj, 'RedirectUrl', None)
                self.Token = getattr(obj, 'Token', None)


