

from .BaseApiResponse import BaseApiResponse


class DeleteLoginResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.LoginId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.LoginId = getattr(obj, 'LoginId', None)


