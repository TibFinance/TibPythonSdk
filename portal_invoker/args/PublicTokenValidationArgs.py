


from ..enums import PublicAccessTokenRoutingType


class PublicTokenValidationArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.TokenType = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.TokenType = PublicAccessTokenRoutingType(getattr(obj, 'TokenType', None)) if getattr(obj, 'TokenType', None) is not None else None


