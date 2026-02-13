

from .BaseApiResponse import BaseApiResponse


class RevertTransferResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.HasBeenDeleted = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.HasBeenDeleted = getattr(obj, 'HasBeenDeleted', None)


