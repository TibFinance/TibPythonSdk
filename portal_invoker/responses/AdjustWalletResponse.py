

from .BaseApiResponse import BaseApiResponse


class AdjustWalletResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.TransferId = None
            self.WasSuccessful = None
            self.RequiresSupplierBoarding = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.TransferId = getattr(obj, 'TransferId', None)
                self.WasSuccessful = getattr(obj, 'WasSuccessful', None)
                self.RequiresSupplierBoarding = getattr(obj, 'RequiresSupplierBoarding', None)


