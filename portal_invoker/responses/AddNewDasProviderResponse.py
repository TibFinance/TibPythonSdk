

from .BaseApiResponse import BaseApiResponse


class AddNewDasProviderResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.DasProviderId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.DasProviderId = getattr(obj, 'DasProviderId', None)


