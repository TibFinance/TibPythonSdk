




class BoardingEventToBroadcast:
    def __init__(self, obj=None):
        if obj is None:
            
            self.BoardingInfoId = None
            self.ClientId = None
            self.CompanyName = None
            self.CompanyAddress = None
            self.CompanyType = None
            self.DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService = None
            self.DidOwnersAlreadyAskedForBankrupcy = None
            self.HaveYouBeenSubjectOfVisaRiskProgram = None
            self.DrivingLicenceNumber = None
            self.BoardingStep = None
            self.CompanyName_Edited = None
            self.CompanyAddress_Edited = None
            self.CompanyType_Edited = None
            self.AccountOwner = None
            self.AccountNumber = None
            self.BankNumber = None
            self.TransitNumber = None
            self.SignedContractContent = None
            self.ClientName = None
            self.ClientEmail = None
            self.ClientPhone = None
            self.CreatedDate = None
            self.SpecimenFile = None
            self.IdFile = None
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
            self.BankPayoutCurrency = None
            self.BankCountryCode = None
            self.BankStateCode = None
            self.BankCity = None
            self.BankName = None
            self.BankRoutingNumber = None
            self.BankBic = None
            self.BankIban = None
            self.BankSortCode = None
            self.BankSwiftCode = None
            self.BankBsb = None
            self.BusinessRegistrationNumber = None
            self.BusinessRegistrationNumber_Edited = None
            self.CompanyLegalName = None
            self.CompanyBusinessType = None
            self.CompanyAccountUserName = None
            self.BankAccountType = None
            self.BankMinimalPayoutAmount = None
            self.BankRefundReserve = None
            self.MerchantServiceAgreementDate = None
            self.MerchantPricingAgreementDate = None
            self.MerchantId = None
            self.Status = None
            self.ErrorResponse = None
            self.ServiceId = None
            self.RequiredDocuments = None
            self.ProviderRequestId = None
            self.CaseId = None
            self.CompanyEmail = None
            self.AverageTransactionAmount = None
            self.HighestTransactionAmount = None
            self.RiskMonitoring = None
            self.RiskPayment = None
            self.RiskByCommission = None
            self.PaymentReference = None
            self.ManagerLinkedIn = None

        else:
            
            self.BoardingInfoId = getattr(obj, 'BoardingInfoId', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.CompanyName = getattr(obj, 'CompanyName', None)
            self.CompanyAddress = getattr(obj, 'CompanyAddress', None)

            self.CompanyType = []
            if hasattr(obj, 'CompanyType') and obj.CompanyType is not None:
                self.CompanyType = [name for name in obj.CompanyType]

            self.DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService = []
            if hasattr(obj, 'DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService') and obj.DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService is not None:
                self.DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService = [name for name in obj.DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService]

            self.DidOwnersAlreadyAskedForBankrupcy = []
            if hasattr(obj, 'DidOwnersAlreadyAskedForBankrupcy') and obj.DidOwnersAlreadyAskedForBankrupcy is not None:
                self.DidOwnersAlreadyAskedForBankrupcy = [name for name in obj.DidOwnersAlreadyAskedForBankrupcy]

            self.HaveYouBeenSubjectOfVisaRiskProgram = []
            if hasattr(obj, 'HaveYouBeenSubjectOfVisaRiskProgram') and obj.HaveYouBeenSubjectOfVisaRiskProgram is not None:
                self.HaveYouBeenSubjectOfVisaRiskProgram = [name for name in obj.HaveYouBeenSubjectOfVisaRiskProgram]
            self.DrivingLicenceNumber = getattr(obj, 'DrivingLicenceNumber', None)
            self.BoardingStep = getattr(obj, 'BoardingStep', None)
            self.CompanyName_Edited = getattr(obj, 'CompanyName_Edited', None)
            self.CompanyAddress_Edited = getattr(obj, 'CompanyAddress_Edited', None)

            self.CompanyType_Edited = []
            if hasattr(obj, 'CompanyType_Edited') and obj.CompanyType_Edited is not None:
                self.CompanyType_Edited = [name for name in obj.CompanyType_Edited]
            self.AccountOwner = getattr(obj, 'AccountOwner', None)
            self.AccountNumber = getattr(obj, 'AccountNumber', None)
            self.BankNumber = getattr(obj, 'BankNumber', None)
            self.TransitNumber = getattr(obj, 'TransitNumber', None)
            self.SignedContractContent = getattr(obj, 'SignedContractContent', None)
            self.ClientName = getattr(obj, 'ClientName', None)
            self.ClientEmail = getattr(obj, 'ClientEmail', None)
            self.ClientPhone = getattr(obj, 'ClientPhone', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.SpecimenFile = getattr(obj, 'SpecimenFile', None)
            self.IdFile = getattr(obj, 'IdFile', None)
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
            self.BankPayoutCurrency = getattr(obj, 'BankPayoutCurrency', None)
            self.BankCountryCode = getattr(obj, 'BankCountryCode', None)
            self.BankStateCode = getattr(obj, 'BankStateCode', None)
            self.BankCity = getattr(obj, 'BankCity', None)
            self.BankName = getattr(obj, 'BankName', None)
            self.BankRoutingNumber = getattr(obj, 'BankRoutingNumber', None)
            self.BankBic = getattr(obj, 'BankBic', None)
            self.BankIban = getattr(obj, 'BankIban', None)
            self.BankSortCode = getattr(obj, 'BankSortCode', None)
            self.BankSwiftCode = getattr(obj, 'BankSwiftCode', None)
            self.BankBsb = getattr(obj, 'BankBsb', None)
            self.BusinessRegistrationNumber = getattr(obj, 'BusinessRegistrationNumber', None)
            self.BusinessRegistrationNumber_Edited = getattr(obj, 'BusinessRegistrationNumber_Edited', None)
            self.CompanyLegalName = getattr(obj, 'CompanyLegalName', None)
            self.CompanyBusinessType = getattr(obj, 'CompanyBusinessType', None)
            self.CompanyAccountUserName = getattr(obj, 'CompanyAccountUserName', None)
            self.BankAccountType = getattr(obj, 'BankAccountType', None)
            self.BankMinimalPayoutAmount = getattr(obj, 'BankMinimalPayoutAmount', None)
            self.BankRefundReserve = getattr(obj, 'BankRefundReserve', None)
            self.MerchantServiceAgreementDate = getattr(obj, 'MerchantServiceAgreementDate', None)
            self.MerchantPricingAgreementDate = getattr(obj, 'MerchantPricingAgreementDate', None)

            self.MerchantId = []
            if hasattr(obj, 'MerchantId') and obj.MerchantId is not None:
                self.MerchantId = [name for name in obj.MerchantId]

            self.Status = []
            if hasattr(obj, 'Status') and obj.Status is not None:
                self.Status = [name for name in obj.Status]
            self.ErrorResponse = getattr(obj, 'ErrorResponse', None)

            self.ServiceId = []
            if hasattr(obj, 'ServiceId') and obj.ServiceId is not None:
                self.ServiceId = [name for name in obj.ServiceId]
            self.RequiredDocuments = getattr(obj, 'RequiredDocuments', None)
            self.ProviderRequestId = getattr(obj, 'ProviderRequestId', None)
            self.CaseId = getattr(obj, 'CaseId', None)
            self.CompanyEmail = getattr(obj, 'CompanyEmail', None)
            self.AverageTransactionAmount = getattr(obj, 'AverageTransactionAmount', None)
            self.HighestTransactionAmount = getattr(obj, 'HighestTransactionAmount', None)
            self.RiskMonitoring = getattr(obj, 'RiskMonitoring', None)
            self.RiskPayment = getattr(obj, 'RiskPayment', None)
            self.RiskByCommission = getattr(obj, 'RiskByCommission', None)
            self.PaymentReference = getattr(obj, 'PaymentReference', None)
            self.ManagerLinkedIn = getattr(obj, 'ManagerLinkedIn', None)


