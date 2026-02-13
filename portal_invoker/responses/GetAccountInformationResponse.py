

from .BaseApiResponse import BaseApiResponse
from ..objects import ProviderAccountOperations


class GetAccountInformationResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ProviderAccountOperationList = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.ProviderAccountOperationList = []
                if hasattr(obj, 'ProviderAccountOperationList') and obj.ProviderAccountOperationList is not None:
                    self.ProviderAccountOperationList = [ProviderAccountOperations(name) for name in  obj.ProviderAccountOperationList]


