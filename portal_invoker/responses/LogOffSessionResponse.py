

from .BaseApiResponse import BaseApiResponse


class LogOffSessionResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.LoggOffSuccess = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.LoggOffSuccess = getattr(obj, 'LoggOffSuccess', None)


