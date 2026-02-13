

from .DasProviderEntityQuebec import DasProviderEntityQuebec


class DasProviderQuebec(DasProviderEntityQuebec):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ProviderId = None

        else:
            super().__init__(obj)

            self.ProviderId = getattr(obj, 'ProviderId', None)


