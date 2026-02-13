

from .BaseApiResponse import BaseApiResponse
from ..enums import PublicAccessTokenRoutingType
from ..objects import WhiteLabeling


class GetPublicTokenRoutingTypeResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.RoutingType = None
            self.WhiteLabeling = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.RoutingType = PublicAccessTokenRoutingType(getattr(obj, 'RoutingType', None)) if getattr(obj, 'RoutingType', None) is not None else None
                self.WhiteLabeling = WhiteLabeling(getattr(obj, 'WhiteLabeling', None)) if getattr(obj, 'WhiteLabeling', None) is not None else None


