

from .BaseApiResponse import BaseApiResponse


class CreateServiceResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CreatedServiceId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.CreatedServiceId = getattr(obj, 'CreatedServiceId', None)


