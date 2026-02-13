

from .BaseApiResponse import BaseApiResponse


class RetreiveDataResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.DataCryptedBase64 = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.DataCryptedBase64 = getattr(obj, 'DataCryptedBase64', None)


