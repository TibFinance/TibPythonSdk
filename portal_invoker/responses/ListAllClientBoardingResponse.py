

from .BaseApiResponse import BaseApiResponse


class ListAllClientBoardingResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.List = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.List = []
                if hasattr(obj, 'List') and obj.List is not None:
                    self.List = [name for name in obj.List]


