

from .BaseApiResponse import BaseApiResponse
from ..objects import LoginRelationsEntity


class GetLoginAccessListResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.LoginRelations = None

        else:
            super().__init__(obj)

            self.LoginRelations = []
            if hasattr(obj, 'LoginRelations') and obj.LoginRelations is not None:
                self.LoginRelations = [LoginRelationsEntity(name) for name in  obj.LoginRelations]


