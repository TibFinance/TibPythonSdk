

from .BaseApiResponse import BaseApiResponse


class CreateSupplierResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.SupplierId = None
            self.SupplierName = None

        else:
            super().__init__(obj)
            self.SupplierId = getattr(obj, 'SupplierId', None)
            self.SupplierName = getattr(obj, 'SupplierName', None)


