

from .BaseApiResponse import BaseApiResponse


class DoesClientExistResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.IsClientExisting = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.IsClientExisting = getattr(obj, 'IsClientExisting', None)


