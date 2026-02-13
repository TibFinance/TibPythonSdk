

from .BaseLoggedSession import BaseLoggedSession


class AdminLoggedInformation(BaseLoggedSession):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.AdminID = None

        else:
            super().__init__(obj)

            self.AdminID = getattr(obj, 'AdminID', None)


