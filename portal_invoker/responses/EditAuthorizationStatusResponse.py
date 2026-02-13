

from .BaseApiResponse import BaseApiResponse


class EditAuthorizationStatusResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.AuthorizationStatus = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.AuthorizationStatus = getattr(obj, 'AuthorizationStatus', None)


