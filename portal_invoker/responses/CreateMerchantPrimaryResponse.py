

from .BaseApiResponse import BaseApiResponse


class CreateMerchantPrimaryResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.MerchantId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.MerchantId = getattr(obj, 'MerchantId', None)


