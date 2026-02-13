


from ..enums import LoginType


class BaseLoggedSession:
    def __init__(self, obj=None):
        if obj is None:
            
            self.LastActivityDate = None
            self.CreationDate = None
            self.LoginsUserRelationsId = None
            self.PermissionType = None

        else:
            
            self.LastActivityDate = getattr(obj, 'LastActivityDate', None)
            self.CreationDate = getattr(obj, 'CreationDate', None)
            self.LoginsUserRelationsId = getattr(obj, 'LoginsUserRelationsId', None)
            self.PermissionType = LoginType(getattr(obj, 'PermissionType', None)) if getattr(obj, 'PermissionType', None) is not None else None


