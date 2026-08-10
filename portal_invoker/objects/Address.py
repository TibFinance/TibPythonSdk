
from ..utility import to_enum

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
            self.ProvinceStateId = to_enum(ProvinceStateId, getattr(obj, 'ProvinceStateId', None))
            self.CountryId = to_enum(CountryId, getattr(obj, 'CountryId', None))
            self.PostalZipCode = getattr(obj, 'PostalZipCode', None)


