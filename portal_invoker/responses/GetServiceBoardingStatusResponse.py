

from .BaseApiResponse import BaseApiResponse
from ..objects import BoardingServiceMerchant


class GetServiceBoardingStatusResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ServiceId = None
            self.BoardingServiceMerchants = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.ServiceId = getattr(obj, 'ServiceId', None)

                self.BoardingServiceMerchants = []
                if hasattr(obj, 'BoardingServiceMerchants') and obj.BoardingServiceMerchants is not None:
                    self.BoardingServiceMerchants = [BoardingServiceMerchant(name) for name in  obj.BoardingServiceMerchants]


