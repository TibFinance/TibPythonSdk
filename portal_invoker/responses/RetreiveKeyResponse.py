

from .BaseApiResponse import BaseApiResponse


class RetreiveKeyResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Key = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Key = getattr(obj, 'Key', None)


