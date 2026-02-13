


from ..enums import CountryId
from ..enums import ProvinceStateId


class ProvinceState:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CountryId = None
            self.CountryAbreviation = None
            self.ProvinceStateId = None
            self.ProvinceAbreviation = None

        else:
            
            self.CountryId = CountryId(getattr(obj, 'CountryId', None)) if getattr(obj, 'CountryId', None) is not None else None
            self.CountryAbreviation = getattr(obj, 'CountryAbreviation', None)
            self.ProvinceStateId = ProvinceStateId(getattr(obj, 'ProvinceStateId', None)) if getattr(obj, 'ProvinceStateId', None) is not None else None
            self.ProvinceAbreviation = getattr(obj, 'ProvinceAbreviation', None)


