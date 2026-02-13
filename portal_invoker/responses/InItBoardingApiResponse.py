

from .BaseApiResponse import BaseApiResponse


class InItBoardingApiResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.NoOfPendingBoarding = None
            self.NoOfActiveBoarding = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.NoOfPendingBoarding = getattr(obj, 'NoOfPendingBoarding', None)
                self.NoOfActiveBoarding = getattr(obj, 'NoOfActiveBoarding', None)


