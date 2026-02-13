

from .BaseApiResponse import BaseApiResponse


class SaveSpecimenResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ClientId = None
            self.MerchantId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.ClientId = getattr(obj, 'ClientId', None)
                self.MerchantId = getattr(obj, 'MerchantId', None)


