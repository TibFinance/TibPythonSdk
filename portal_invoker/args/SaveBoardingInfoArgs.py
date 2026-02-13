


from ..objects import BoardingInfoFileEntity


class SaveBoardingInfoArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.BusinessRegistrationNumber = None
            self.BusinessRegistrationNumber_Edited = None
            self.CompanyName = None
            self.CompanyAddress = None
            self.AdminFirstName = None
            self.AdminLastName = None
            self.AdminAddress = None
            self.ManagerFirstName = None
            self.ManagerLastName = None
            self.ManagerAddress = None
            self.ManagerFirstName2 = None
            self.ManagerLastName2 = None
            self.ManagerAddress2 = None
            self.ManagerLinkedIn = None
            self.ManagerIsAlsoAdmin = None
            self.CompanyType = None
            self.CompanyName2 = None
            self.CompanyAddress2 = None
            self.AdminFirstName2 = None
            self.AdminLastName2 = None
            self.AdminAddress2 = None
            self.CompanyType2 = None
            self.DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService = None
            self.DidOwnersAlreadyAskedForBankrupcy = None
            self.HaveYouBeenSubjectOfVisaRiskProgram = None
            self.IdImageAsBase64 = None
            self.AdminIdImageFront = None
            self.AdminIdImageBack = None
            self.ManagerIdImageFront = None
            self.ManagerIdImageBack = None
            self.IdFiles = None
            self.CompanyTaxId = None
            self.CompanyCountryCode = None
            self.CompanyStateCode = None
            self.CompanyCity = None
            self.CompanyZip = None
            self.CompanyPhone = None
            self.CompanyProductAndServiceDescription = None
            self.CompanyWebSite = None
            self.CompanyBusinessCategory = None
            self.CompanySalesVolume = None
            self.AdminCountryCode = None
            self.AdminStateCode = None
            self.AdminCity = None
            self.AdminZip = None
            self.AdminPhone = None
            self.AdminBirthDate = None
            self.AdminGovId = None
            self.ManagerCountryCode = None
            self.ManagerStateCode = None
            self.ManagerCity = None
            self.ManagerZip = None
            self.ManagerPhone = None
            self.ManagerBirthDate = None
            self.ManagerGovId = None
            self.BankPayoutCurrency = None
            self.BankCountryCode = None
            self.BankStateCode = None
            self.BankCity = None
            self.BankName = None
            self.BankNumber = None
            self.BankTransitNumber = None
            self.BankAccountNumber = None
            self.BankRoutingNumber = None
            self.BankBic = None
            self.BankIban = None
            self.BankSortCode = None
            self.BankSwiftCode = None
            self.BankBsb = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.BusinessRegistrationNumber = getattr(obj, 'BusinessRegistrationNumber', None)
            self.BusinessRegistrationNumber_Edited = getattr(obj, 'BusinessRegistrationNumber_Edited', None)
            self.CompanyName = getattr(obj, 'CompanyName', None)
            self.CompanyAddress = getattr(obj, 'CompanyAddress', None)
            self.AdminFirstName = getattr(obj, 'AdminFirstName', None)
            self.AdminLastName = getattr(obj, 'AdminLastName', None)
            self.AdminAddress = getattr(obj, 'AdminAddress', None)
            self.ManagerFirstName = getattr(obj, 'ManagerFirstName', None)
            self.ManagerLastName = getattr(obj, 'ManagerLastName', None)
            self.ManagerAddress = getattr(obj, 'ManagerAddress', None)
            self.ManagerFirstName2 = getattr(obj, 'ManagerFirstName2', None)
            self.ManagerLastName2 = getattr(obj, 'ManagerLastName2', None)
            self.ManagerAddress2 = getattr(obj, 'ManagerAddress2', None)
            self.ManagerLinkedIn = getattr(obj, 'ManagerLinkedIn', None)
            self.ManagerIsAlsoAdmin = getattr(obj, 'ManagerIsAlsoAdmin', None)
            self.CompanyType = getattr(obj, 'CompanyType', None)
            self.CompanyName2 = getattr(obj, 'CompanyName2', None)
            self.CompanyAddress2 = getattr(obj, 'CompanyAddress2', None)
            self.AdminFirstName2 = getattr(obj, 'AdminFirstName2', None)
            self.AdminLastName2 = getattr(obj, 'AdminLastName2', None)
            self.AdminAddress2 = getattr(obj, 'AdminAddress2', None)
            self.CompanyType2 = getattr(obj, 'CompanyType2', None)
            self.DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService = getattr(obj, 'DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService', None)
            self.DidOwnersAlreadyAskedForBankrupcy = getattr(obj, 'DidOwnersAlreadyAskedForBankrupcy', None)
            self.HaveYouBeenSubjectOfVisaRiskProgram = getattr(obj, 'HaveYouBeenSubjectOfVisaRiskProgram', None)
            self.IdImageAsBase64 = getattr(obj, 'IdImageAsBase64', None)
            self.AdminIdImageFront = getattr(obj, 'AdminIdImageFront', None)
            self.AdminIdImageBack = getattr(obj, 'AdminIdImageBack', None)
            self.ManagerIdImageFront = getattr(obj, 'ManagerIdImageFront', None)
            self.ManagerIdImageBack = getattr(obj, 'ManagerIdImageBack', None)

            self.IdFiles = []
            if hasattr(obj, 'IdFiles') and obj.IdFiles is not None:
                self.IdFiles = [BoardingInfoFileEntity(name) for name in  obj.IdFiles]
            self.CompanyTaxId = getattr(obj, 'CompanyTaxId', None)
            self.CompanyCountryCode = getattr(obj, 'CompanyCountryCode', None)
            self.CompanyStateCode = getattr(obj, 'CompanyStateCode', None)
            self.CompanyCity = getattr(obj, 'CompanyCity', None)
            self.CompanyZip = getattr(obj, 'CompanyZip', None)
            self.CompanyPhone = getattr(obj, 'CompanyPhone', None)
            self.CompanyProductAndServiceDescription = getattr(obj, 'CompanyProductAndServiceDescription', None)
            self.CompanyWebSite = getattr(obj, 'CompanyWebSite', None)
            self.CompanyBusinessCategory = getattr(obj, 'CompanyBusinessCategory', None)
            self.CompanySalesVolume = getattr(obj, 'CompanySalesVolume', None)
            self.AdminCountryCode = getattr(obj, 'AdminCountryCode', None)
            self.AdminStateCode = getattr(obj, 'AdminStateCode', None)
            self.AdminCity = getattr(obj, 'AdminCity', None)
            self.AdminZip = getattr(obj, 'AdminZip', None)
            self.AdminPhone = getattr(obj, 'AdminPhone', None)
            self.AdminBirthDate = getattr(obj, 'AdminBirthDate', None)
            self.AdminGovId = getattr(obj, 'AdminGovId', None)
            self.ManagerCountryCode = getattr(obj, 'ManagerCountryCode', None)
            self.ManagerStateCode = getattr(obj, 'ManagerStateCode', None)
            self.ManagerCity = getattr(obj, 'ManagerCity', None)
            self.ManagerZip = getattr(obj, 'ManagerZip', None)
            self.ManagerPhone = getattr(obj, 'ManagerPhone', None)
            self.ManagerBirthDate = getattr(obj, 'ManagerBirthDate', None)
            self.ManagerGovId = getattr(obj, 'ManagerGovId', None)
            self.BankPayoutCurrency = getattr(obj, 'BankPayoutCurrency', None)
            self.BankCountryCode = getattr(obj, 'BankCountryCode', None)
            self.BankStateCode = getattr(obj, 'BankStateCode', None)
            self.BankCity = getattr(obj, 'BankCity', None)
            self.BankName = getattr(obj, 'BankName', None)
            self.BankNumber = getattr(obj, 'BankNumber', None)
            self.BankTransitNumber = getattr(obj, 'BankTransitNumber', None)
            self.BankAccountNumber = getattr(obj, 'BankAccountNumber', None)
            self.BankRoutingNumber = getattr(obj, 'BankRoutingNumber', None)
            self.BankBic = getattr(obj, 'BankBic', None)
            self.BankIban = getattr(obj, 'BankIban', None)
            self.BankSortCode = getattr(obj, 'BankSortCode', None)
            self.BankSwiftCode = getattr(obj, 'BankSwiftCode', None)
            self.BankBsb = getattr(obj, 'BankBsb', None)


