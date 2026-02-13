

from .BoardingInfoEntity import BoardingInfoEntity


class BoardingInfo(BoardingInfoEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BoardingInfoId = None
            self.AdminBirthDate = None
            self.AdminZip = None
            self.AdminCountryCode = None
            self.AdminStateCode = None
            self.AdminPhone = None
            self.AdminGovId = None
            self.ManagerBirthDate = None
            self.ManagerZip = None
            self.ManagerStateCode = None
            self.ManagerPhone = None
            self.ManagerCountryCode = None
            self.ManagerGovId = None
            self.ManagerAddress_Edited = None
            self.ManagerFirstName_Edited = None
            self.ManagerLastName_Edited = None
            self.CompanyCountryCode = None
            self.CompanyCity = None
            self.CompanyZip = None
            self.CompanyStateCode = None
            self.CompanyTaxId = None
            self.CompanyWebSite = None
            self.CompanySalesVolume = None
            self.CompanyProductAndServiceDescription = None
            self.BusinessRegistrationNumber = None
            self.BusinessRegistrationNumber_Edited = None
            self.BankBic = None
            self.BankIban = None
            self.BankCity = None
            self.BankStateCode = None
            self.BankCountryCode = None
            self.BankName = None
            self.BankRoutingNumber = None
            self.BankPayoutCurrency = None
            self.BankSortCode = None
            self.BankBsb = None
            self.BankSwiftCode = None
            self.CompanyBusinessCategory = None
            self.AdminCity = None
            self.ManagerCity = None
            self.Files = None

        else:
            super().__init__(obj)

            from .BoardingInfoFileEntity import BoardingInfoFileEntity
            self.BoardingInfoId = getattr(obj, 'BoardingInfoId', None)
            self.AdminBirthDate = getattr(obj, 'AdminBirthDate', None)
            self.AdminZip = getattr(obj, 'AdminZip', None)
            self.AdminCountryCode = getattr(obj, 'AdminCountryCode', None)
            self.AdminStateCode = getattr(obj, 'AdminStateCode', None)
            self.AdminPhone = getattr(obj, 'AdminPhone', None)
            self.AdminGovId = getattr(obj, 'AdminGovId', None)
            self.ManagerBirthDate = getattr(obj, 'ManagerBirthDate', None)
            self.ManagerZip = getattr(obj, 'ManagerZip', None)
            self.ManagerStateCode = getattr(obj, 'ManagerStateCode', None)
            self.ManagerPhone = getattr(obj, 'ManagerPhone', None)
            self.ManagerCountryCode = getattr(obj, 'ManagerCountryCode', None)
            self.ManagerGovId = getattr(obj, 'ManagerGovId', None)
            self.ManagerAddress_Edited = getattr(obj, 'ManagerAddress_Edited', None)
            self.ManagerFirstName_Edited = getattr(obj, 'ManagerFirstName_Edited', None)
            self.ManagerLastName_Edited = getattr(obj, 'ManagerLastName_Edited', None)
            self.CompanyCountryCode = getattr(obj, 'CompanyCountryCode', None)
            self.CompanyCity = getattr(obj, 'CompanyCity', None)
            self.CompanyZip = getattr(obj, 'CompanyZip', None)
            self.CompanyStateCode = getattr(obj, 'CompanyStateCode', None)
            self.CompanyTaxId = getattr(obj, 'CompanyTaxId', None)
            self.CompanyWebSite = getattr(obj, 'CompanyWebSite', None)
            self.CompanySalesVolume = getattr(obj, 'CompanySalesVolume', None)
            self.CompanyProductAndServiceDescription = getattr(obj, 'CompanyProductAndServiceDescription', None)
            self.BusinessRegistrationNumber = getattr(obj, 'BusinessRegistrationNumber', None)
            self.BusinessRegistrationNumber_Edited = getattr(obj, 'BusinessRegistrationNumber_Edited', None)
            self.BankBic = getattr(obj, 'BankBic', None)
            self.BankIban = getattr(obj, 'BankIban', None)
            self.BankCity = getattr(obj, 'BankCity', None)
            self.BankStateCode = getattr(obj, 'BankStateCode', None)
            self.BankCountryCode = getattr(obj, 'BankCountryCode', None)
            self.BankName = getattr(obj, 'BankName', None)
            self.BankRoutingNumber = getattr(obj, 'BankRoutingNumber', None)
            self.BankPayoutCurrency = getattr(obj, 'BankPayoutCurrency', None)
            self.BankSortCode = getattr(obj, 'BankSortCode', None)
            self.BankBsb = getattr(obj, 'BankBsb', None)
            self.BankSwiftCode = getattr(obj, 'BankSwiftCode', None)
            self.CompanyBusinessCategory = getattr(obj, 'CompanyBusinessCategory', None)
            self.AdminCity = getattr(obj, 'AdminCity', None)
            self.ManagerCity = getattr(obj, 'ManagerCity', None)

            self.Files = []
            if hasattr(obj, 'Files') and obj.Files is not None:
                self.Files = [BoardingInfoFileEntity(name) for name in  obj.Files]


