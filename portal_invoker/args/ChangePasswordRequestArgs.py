


from ..enums import PublicAccessTokenRoutingType


class ChangePasswordRequestArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.Username = None
            self.RoutingType = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.Username = getattr(obj, 'Username', None)
            self.RoutingType = PublicAccessTokenRoutingType(getattr(obj, 'RoutingType', None)) if getattr(obj, 'RoutingType', None) is not None else None


