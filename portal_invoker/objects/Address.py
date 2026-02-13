


from ..enums import ProvinceStateId
from ..enums import CountryId


class Address:
    def __init__(self, obj=None):
        if obj is None:
            
            self.StreetAddress = None
            self.AddressCity = None
            self.ProvinceStateId = None
            self.CountryId = None
            self.PostalZipCode = None

        else:
            
            self.StreetAddress = getattr(obj, 'StreetAddress', None)
            self.AddressCity = getattr(obj, 'AddressCity', None)
            self.ProvinceStateId = ProvinceStateId(getattr(obj, 'ProvinceStateId', None)) if getattr(obj, 'ProvinceStateId', None) is not None else None
            self.CountryId = CountryId(getattr(obj, 'CountryId', None)) if getattr(obj, 'CountryId', None) is not None else None
            self.PostalZipCode = getattr(obj, 'PostalZipCode', None)


