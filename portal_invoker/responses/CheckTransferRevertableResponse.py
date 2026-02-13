

from .BaseApiResponse import BaseApiResponse


class CheckTransferRevertableResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.IsRevertable = None
            self.Reason = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.IsRevertable = getattr(obj, 'IsRevertable', None)
                self.Reason = getattr(obj, 'Reason', None)


