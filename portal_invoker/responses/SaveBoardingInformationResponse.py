

from .BaseApiResponse import BaseApiResponse


class SaveBoardingInformationResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BoardingInformationId = None
            self.MerchantId = None
            self.Message = None
            self.BoardingStatus = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.BoardingInformationId = getattr(obj, 'BoardingInformationId', None)
                self.MerchantId = getattr(obj, 'MerchantId', None)
                self.Message = getattr(obj, 'Message', None)
                self.BoardingStatus = getattr(obj, 'BoardingStatus', None)


