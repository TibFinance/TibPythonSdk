

from .BaseApiResponse import BaseApiResponse


class GetDropInPublicTokenResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.PublicTokenId = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.PublicTokenId = getattr(obj, 'PublicTokenId', None)


