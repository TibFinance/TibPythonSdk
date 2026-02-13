

from .BaseApiResponse import BaseApiResponse


class GetFeesOverloadMerchantResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.FeesOverLoadMerchantId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.FeesOverLoadMerchantId = getattr(obj, 'FeesOverLoadMerchantId', None)


