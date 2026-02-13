


from ..objects import ServiceEntity
from ..objects import Address
from ..objects import ServiceFeeSettings
from ..objects import ServiceSettings
from ..enums import Currency
from ..enums import Language


class CreateServiceFromPublicTokenArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.Service = None
            self.Address = None
            self.ServicesFee = None
            self.ServiceSettings = None
            self.AccountName = None
            self.IsPrimary = None
            self.BankAddress = None
            self.BankCity = None
            self.BankProvince = None
            self.BankCountry = None
            self.BankName = None
            self.BankNumber = None
            self.BankTransit = None
            self.BankAccount = None
            self.OwnerEmail = None
            self.Currency = None
            self.Language = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.Service = ServiceEntity(getattr(obj, 'Service', None)) if getattr(obj, 'Service', None) is not None else None
            self.Address = Address(getattr(obj, 'Address', None)) if getattr(obj, 'Address', None) is not None else None
            self.ServicesFee = ServiceFeeSettings(getattr(obj, 'ServicesFee', None)) if getattr(obj, 'ServicesFee', None) is not None else None
            self.ServiceSettings = ServiceSettings(getattr(obj, 'ServiceSettings', None)) if getattr(obj, 'ServiceSettings', None) is not None else None
            self.AccountName = getattr(obj, 'AccountName', None)
            self.IsPrimary = getattr(obj, 'IsPrimary', None)
            self.BankAddress = getattr(obj, 'BankAddress', None)
            self.BankCity = getattr(obj, 'BankCity', None)
            self.BankProvince = getattr(obj, 'BankProvince', None)
            self.BankCountry = getattr(obj, 'BankCountry', None)
            self.BankName = getattr(obj, 'BankName', None)
            self.BankNumber = getattr(obj, 'BankNumber', None)
            self.BankTransit = getattr(obj, 'BankTransit', None)
            self.BankAccount = getattr(obj, 'BankAccount', None)
            self.OwnerEmail = getattr(obj, 'OwnerEmail', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None


