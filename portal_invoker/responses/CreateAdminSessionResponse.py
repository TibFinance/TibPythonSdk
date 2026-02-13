

from .BaseApiResponse import BaseApiResponse


class CreateAdminSessionResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.SessionId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.SessionId = getattr(obj, 'SessionId', None)


