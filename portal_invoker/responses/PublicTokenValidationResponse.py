

from .BaseApiResponse import BaseApiResponse


class PublicTokenValidationResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.IsValid = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.IsValid = getattr(obj, 'IsValid', None)


