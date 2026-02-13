

from .BaseApiResponse import BaseApiResponse
from ..objects import ClientLogin


class GetClientUsersResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Users = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.Users = []
                if hasattr(obj, 'Users') and obj.Users is not None:
                    self.Users = [ClientLogin(name) for name in  obj.Users]


