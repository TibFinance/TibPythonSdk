

from .BoardingInformationEntity import BoardingInformationEntity


class BoardingInformation(BoardingInformationEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BoardingInfoId = None
            self.ServiceId = None
            self.MerchantId = None
            self.CreatedDate = None
            self.ProviderRequestId = None
            self.CaseId = None
            self.CompanyCountryCode = None
            self.CompanyCity = None
            self.CompanyZip = None
            self.CompanyStateCode = None
            self.CompanyTaxId = None
            self.CompanyWebSite = None
            self.CompanySalesVolume = None
            self.CompanyProductAndServiceDescription = None
            self.BusinessRegistrationNumber = None
            self.AverageTransactionAmount = None
            self.HighestTransactionAmount = None
            self.RiskMonitoring = None
            self.RiskPayment = None
            self.RiskByCommission = None
            self.BusinessRegistrationNumber_Edited = None
            self.BankBic = None
            self.BankIban = None
            self.BankCity = None
            self.BankStateCode = None
            self.BankCountryCode = None
            self.BankName = None
            self.BankRoutingNumber = None
            self.BankAccountNumber = None
            self.BankTransitNumber = None
            self.BankPayoutCurrency = None
            self.BankSortCode = None
            self.BankBsb = None
            self.BankSwiftCode = None
            self.CompanyBusinessCategory = None
            self.CompanyLegalName = None
            self.CompanyBusinessType = None
            self.CompanyAccountUserName = None
            self.BankAccountType = None
            self.BankMinimalPayoutAmount = None
            self.BankRefundReserve = None
            self.MerchantServiceAgreementDate = None
            self.MerchantPricingAgreementDate = None
            self.Status = None
            self.ErrorResponse = None
            self.Files = None
            self.ClientName = None
            self.ClientEmail = None
            self.PhoneNumber = None
            self.CompanyMerchantLanguage = None
            self.Currency = None
            self.Persons = None

        else:
            super().__init__(obj)

            from .BoardingInformationFileEntity import BoardingInformationFileEntity
            from .BoardingInfoPersonEntity import BoardingInfoPersonEntity
            self.BoardingInfoId = getattr(obj, 'BoardingInfoId', None)

            self.ServiceId = []
            if hasattr(obj, 'ServiceId') and obj.ServiceId is not None:
                self.ServiceId = [name for name in obj.ServiceId]

            self.MerchantId = []
            if hasattr(obj, 'MerchantId') and obj.MerchantId is not None:
                self.MerchantId = [name for name in obj.MerchantId]

            self.CreatedDate = []
            if hasattr(obj, 'CreatedDate') and obj.CreatedDate is not None:
                self.CreatedDate = [name for name in obj.CreatedDate]
            self.ProviderRequestId = getattr(obj, 'ProviderRequestId', None)
            self.CaseId = getattr(obj, 'CaseId', None)
            self.CompanyCountryCode = getattr(obj, 'CompanyCountryCode', None)
            self.CompanyCity = getattr(obj, 'CompanyCity', None)
            self.CompanyZip = getattr(obj, 'CompanyZip', None)
            self.CompanyStateCode = getattr(obj, 'CompanyStateCode', None)
            self.CompanyTaxId = getattr(obj, 'CompanyTaxId', None)
            self.CompanyWebSite = getattr(obj, 'CompanyWebSite', None)
            self.CompanySalesVolume = getattr(obj, 'CompanySalesVolume', None)
            self.CompanyProductAndServiceDescription = getattr(obj, 'CompanyProductAndServiceDescription', None)
            self.BusinessRegistrationNumber = getattr(obj, 'BusinessRegistrationNumber', None)
            self.AverageTransactionAmount = getattr(obj, 'AverageTransactionAmount', None)
            self.HighestTransactionAmount = getattr(obj, 'HighestTransactionAmount', None)
            self.RiskMonitoring = getattr(obj, 'RiskMonitoring', None)
            self.RiskPayment = getattr(obj, 'RiskPayment', None)
            self.RiskByCommission = getattr(obj, 'RiskByCommission', None)
            self.BusinessRegistrationNumber_Edited = getattr(obj, 'BusinessRegistrationNumber_Edited', None)
            self.BankBic = getattr(obj, 'BankBic', None)
            self.BankIban = getattr(obj, 'BankIban', None)
            self.BankCity = getattr(obj, 'BankCity', None)
            self.BankStateCode = getattr(obj, 'BankStateCode', None)
            self.BankCountryCode = getattr(obj, 'BankCountryCode', None)
            self.BankName = getattr(obj, 'BankName', None)
            self.BankRoutingNumber = getattr(obj, 'BankRoutingNumber', None)
            self.BankAccountNumber = getattr(obj, 'BankAccountNumber', None)
            self.BankTransitNumber = getattr(obj, 'BankTransitNumber', None)
            self.BankPayoutCurrency = getattr(obj, 'BankPayoutCurrency', None)
            self.BankSortCode = getattr(obj, 'BankSortCode', None)
            self.BankBsb = getattr(obj, 'BankBsb', None)
            self.BankSwiftCode = getattr(obj, 'BankSwiftCode', None)
            self.CompanyBusinessCategory = getattr(obj, 'CompanyBusinessCategory', None)
            self.CompanyLegalName = getattr(obj, 'CompanyLegalName', None)
            self.CompanyBusinessType = getattr(obj, 'CompanyBusinessType', None)
            self.CompanyAccountUserName = getattr(obj, 'CompanyAccountUserName', None)
            self.BankAccountType = getattr(obj, 'BankAccountType', None)
            self.BankMinimalPayoutAmount = getattr(obj, 'BankMinimalPayoutAmount', None)
            self.BankRefundReserve = getattr(obj, 'BankRefundReserve', None)
            self.MerchantServiceAgreementDate = getattr(obj, 'MerchantServiceAgreementDate', None)
            self.MerchantPricingAgreementDate = getattr(obj, 'MerchantPricingAgreementDate', None)

            self.Status = []
            if hasattr(obj, 'Status') and obj.Status is not None:
                self.Status = [name for name in obj.Status]
            self.ErrorResponse = getattr(obj, 'ErrorResponse', None)

            self.Files = []
            if hasattr(obj, 'Files') and obj.Files is not None:
                self.Files = [BoardingInformationFileEntity(name) for name in  obj.Files]
            self.ClientName = getattr(obj, 'ClientName', None)
            self.ClientEmail = getattr(obj, 'ClientEmail', None)
            self.PhoneNumber = getattr(obj, 'PhoneNumber', None)
            self.CompanyMerchantLanguage = getattr(obj, 'CompanyMerchantLanguage', None)
            self.Currency = getattr(obj, 'Currency', None)

            self.Persons = []
            if hasattr(obj, 'Persons') and obj.Persons is not None:
                self.Persons = [BoardingInfoPersonEntity(name) for name in  obj.Persons]


