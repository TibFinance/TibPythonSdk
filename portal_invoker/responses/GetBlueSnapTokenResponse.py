

from .BaseApiResponse import BaseApiResponse
from ..responses import GetBlueSnapClientTokenResponse


class GetBlueSnapTokenResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.GetBlueSnapClientTokenResponse = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.GetBlueSnapClientTokenResponse = GetBlueSnapClientTokenResponse(getattr(obj, 'GetBlueSnapClientTokenResponse', None)) if getattr(obj, 'GetBlueSnapClientTokenResponse', None) is not None else None


