

from .BaseApiResponse import BaseApiResponse


class LoadCompanyTypesResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CompanyTypes = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.CompanyTypes = getattr(obj, 'CompanyTypes', None)


