

from .BaseApiResponse import BaseApiResponse
from ..objects import GetBlueSnapClientTokenResultEntity


class GetBlueSnapClientTokenResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.GetBlueSnapClientTokenResultEntity = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.GetBlueSnapClientTokenResultEntity = GetBlueSnapClientTokenResultEntity(getattr(obj, 'GetBlueSnapClientTokenResultEntity', None)) if getattr(obj, 'GetBlueSnapClientTokenResultEntity', None) is not None else None


