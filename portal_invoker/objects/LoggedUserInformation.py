

from .BaseLoggedSession import BaseLoggedSession


class LoggedUserInformation(BaseLoggedSession):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.InternalReferenceId = None
            self.LoginId = None
            self.UserClientId = None
            self.Username = None
            self.UserFirstName = None
            self.UserLastName = None
            self.IsManagerAccount = None
            self.Description = None
            self.IsReadOnly = None

        else:
            super().__init__(obj)

            self.InternalReferenceId = getattr(obj, 'InternalReferenceId', None)
            self.LoginId = getattr(obj, 'LoginId', None)
            self.UserClientId = getattr(obj, 'UserClientId', None)
            self.Username = getattr(obj, 'Username', None)
            self.UserFirstName = getattr(obj, 'UserFirstName', None)
            self.UserLastName = getattr(obj, 'UserLastName', None)
            self.IsManagerAccount = getattr(obj, 'IsManagerAccount', None)
            self.Description = getattr(obj, 'Description', None)
            self.IsReadOnly = getattr(obj, 'IsReadOnly', None)


