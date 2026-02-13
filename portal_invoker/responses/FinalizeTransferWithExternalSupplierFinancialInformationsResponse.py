

from .BaseApiResponse import BaseApiResponse


class FinalizeTransferWithExternalSupplierFinancialInformationsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Link = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Link = getattr(obj, 'Link', None)


