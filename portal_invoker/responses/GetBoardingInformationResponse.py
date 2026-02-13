

from .BaseApiResponse import BaseApiResponse
from ..objects import BoardingInformation


class GetBoardingInformationResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BoardingInfo = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.BoardingInfo = BoardingInformation(getattr(obj, 'BoardingInfo', None)) if getattr(obj, 'BoardingInfo', None) is not None else None


