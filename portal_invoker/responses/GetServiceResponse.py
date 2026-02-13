

from .BaseApiResponse import BaseApiResponse
from ..objects import ServiceWithMerchant


class GetServiceResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Service = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Service = ServiceWithMerchant(getattr(obj, 'Service', None)) if getattr(obj, 'Service', None) is not None else None


