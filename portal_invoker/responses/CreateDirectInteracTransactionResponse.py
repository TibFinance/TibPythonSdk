

from .BaseApiResponse import BaseApiResponse


class CreateDirectInteracTransactionResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.TransferId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.TransferId = getattr(obj, 'TransferId', None)


