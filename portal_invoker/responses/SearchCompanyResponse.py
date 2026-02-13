

from .BaseApiResponse import BaseApiResponse


class SearchCompanyResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.NeqOrNi = None
            self.CompanyName = None
            self.AddressDisplay = None
            self.CreationDate = None
            self.IsQuebec = None
            self.HasDetails = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.NeqOrNi = getattr(obj, 'NeqOrNi', None)
                self.CompanyName = getattr(obj, 'CompanyName', None)
                self.AddressDisplay = getattr(obj, 'AddressDisplay', None)
                self.CreationDate = getattr(obj, 'CreationDate', None)
                self.IsQuebec = getattr(obj, 'IsQuebec', None)
                self.HasDetails = getattr(obj, 'HasDetails', None)


