

from .BaseApiResponse import BaseApiResponse
from ..objects import Wallet


class GetWalletInformationsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Wallets = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.Wallets = []
                if hasattr(obj, 'Wallets') and obj.Wallets is not None:
                    self.Wallets = [Wallet(name) for name in  obj.Wallets]


