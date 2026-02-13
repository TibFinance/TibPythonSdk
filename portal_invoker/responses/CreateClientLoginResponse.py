

from .BaseApiResponse import BaseApiResponse


class CreateClientLoginResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ClientLoginId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.ClientLoginId = getattr(obj, 'ClientLoginId', None)


