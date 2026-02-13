

from .BaseApiResponse import BaseApiResponse


class GetSessionCookiesAdminResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ClientId = None
            self.ServiceId = None
            self.SessionId = None
            self.LoginTypeId = None
            self.Username = None
            self.Language = None
            self.IsReadOnly = None
            self.InternalReferenceId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.ClientId = getattr(obj, 'ClientId', None)
                self.ServiceId = getattr(obj, 'ServiceId', None)
                self.SessionId = getattr(obj, 'SessionId', None)
                self.LoginTypeId = getattr(obj, 'LoginTypeId', None)
                self.Username = getattr(obj, 'Username', None)
                self.Language = getattr(obj, 'Language', None)
                self.IsReadOnly = getattr(obj, 'IsReadOnly', None)
                self.InternalReferenceId = getattr(obj, 'InternalReferenceId', None)


