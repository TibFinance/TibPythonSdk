

from .BaseApiResponse import BaseApiResponse


class GetSuppliersResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Suppliers = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.Suppliers = []
                if hasattr(obj, 'Suppliers') and obj.Suppliers is not None:
                    self.Suppliers = [name for name in obj.Suppliers]


