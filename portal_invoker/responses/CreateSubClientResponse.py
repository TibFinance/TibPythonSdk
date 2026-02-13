

from .BaseApiResponse import BaseApiResponse


class CreateSubClientResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ServiceId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.ServiceId = getattr(obj, 'ServiceId', None)


