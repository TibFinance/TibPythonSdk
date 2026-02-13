

from .BaseApiResponse import BaseApiResponse


class CollectMerchantResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            pass
        else:
            super().__init__(obj)
            if not obj.HasError:
                pass

