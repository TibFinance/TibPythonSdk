

from .BaseApiResponse import BaseApiResponse


class GetNewKeyResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Token = None
            self.Key = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Token = getattr(obj, 'Token', None)
                self.Key = getattr(obj, 'Key', None)


