

from .BaseApiResponse import BaseApiResponse


class PushDataResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.DataId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.DataId = getattr(obj, 'DataId', None)


