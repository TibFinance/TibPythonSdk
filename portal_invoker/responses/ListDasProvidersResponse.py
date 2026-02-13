

from .BaseApiResponse import BaseApiResponse
from ..objects import DasProviderCanada
from ..objects import DasProviderQuebec


class ListDasProvidersResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CanadaDasProvider = None
            self.QuebecDasProvider = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.CanadaDasProvider = []
                if hasattr(obj, 'CanadaDasProvider') and obj.CanadaDasProvider is not None:
                    self.CanadaDasProvider = [DasProviderCanada(name) for name in  obj.CanadaDasProvider]

                self.QuebecDasProvider = []
                if hasattr(obj, 'QuebecDasProvider') and obj.QuebecDasProvider is not None:
                    self.QuebecDasProvider = [DasProviderQuebec(name) for name in  obj.QuebecDasProvider]


