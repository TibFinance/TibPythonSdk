

from .BaseApiResponse import BaseApiResponse


class DeleteLoginRelationResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.LoginRelationId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.LoginRelationId = getattr(obj, 'LoginRelationId', None)


