

from .BaseApiResponse import BaseApiResponse


class CreateClientResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ClientId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.ClientId = getattr(obj, 'ClientId', None)


