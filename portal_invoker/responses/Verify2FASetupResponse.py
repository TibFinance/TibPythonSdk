

from .BaseApiResponse import BaseApiResponse


class Verify2FASetupResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Success = None
            self.Message = None
            self.ErrorMessage = None

        else:
            super().__init__(obj)
            self.Success = getattr(obj, 'Success', None)
            self.Message = getattr(obj, 'Message', None)
            self.ErrorMessage = getattr(obj, 'ErrorMessage', None)


