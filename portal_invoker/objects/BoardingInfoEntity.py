




class BoardingInfoEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ClientId = None
            self.CompanyName = None
            self.CompanyAddress = None
            self.CompanyPhone = None
            self.CompanyEmail = None
            self.AdminFirstName = None
            self.AdminLastName = None
            self.AdminAddress = None
            self.IsManagerAlsoAdmin = None
            self.ManagerFirstName = None
            self.ManagerLastName = None
            self.ManagerAddress = None
            self.ManagerLinkedIn = None
            self.CompanyType = None
            self.CompanyName_Edited = None
            self.CompanyAddress_Edited = None
            self.CompanyType_Edited = None
            self.AdminFirstName_Edited = None
            self.AdminLastName_Edited = None
            self.AdminAddress_Edited = None
            self.DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService = None
            self.DidOwnersAlreadyAskedForBankrupcy = None
            self.HaveYouBeenSubjectOfVisaRiskProgram = None
            self.SpecimenFile = None
            self.IdFile = None
            self.BoardingStep = None
            self.TransitNumber = None
            self.AccountNumber = None
            self.AccountOwner = None
            self.BankNumber = None

        else:
            
            self.ClientId = getattr(obj, 'ClientId', None)
            self.CompanyName = getattr(obj, 'CompanyName', None)
            self.CompanyAddress = getattr(obj, 'CompanyAddress', None)
            self.CompanyPhone = getattr(obj, 'CompanyPhone', None)
            self.CompanyEmail = getattr(obj, 'CompanyEmail', None)
            self.AdminFirstName = getattr(obj, 'AdminFirstName', None)
            self.AdminLastName = getattr(obj, 'AdminLastName', None)
            self.AdminAddress = getattr(obj, 'AdminAddress', None)
            self.IsManagerAlsoAdmin = getattr(obj, 'IsManagerAlsoAdmin', None)
            self.ManagerFirstName = getattr(obj, 'ManagerFirstName', None)
            self.ManagerLastName = getattr(obj, 'ManagerLastName', None)
            self.ManagerAddress = getattr(obj, 'ManagerAddress', None)
            self.ManagerLinkedIn = getattr(obj, 'ManagerLinkedIn', None)
            self.CompanyType = getattr(obj, 'CompanyType', None)
            self.CompanyName_Edited = getattr(obj, 'CompanyName_Edited', None)
            self.CompanyAddress_Edited = getattr(obj, 'CompanyAddress_Edited', None)
            self.CompanyType_Edited = getattr(obj, 'CompanyType_Edited', None)
            self.AdminFirstName_Edited = getattr(obj, 'AdminFirstName_Edited', None)
            self.AdminLastName_Edited = getattr(obj, 'AdminLastName_Edited', None)
            self.AdminAddress_Edited = getattr(obj, 'AdminAddress_Edited', None)
            self.DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService = getattr(obj, 'DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService', None)
            self.DidOwnersAlreadyAskedForBankrupcy = getattr(obj, 'DidOwnersAlreadyAskedForBankrupcy', None)
            self.HaveYouBeenSubjectOfVisaRiskProgram = getattr(obj, 'HaveYouBeenSubjectOfVisaRiskProgram', None)
            self.SpecimenFile = getattr(obj, 'SpecimenFile', None)
            self.IdFile = getattr(obj, 'IdFile', None)
            self.BoardingStep = getattr(obj, 'BoardingStep', None)
            self.TransitNumber = getattr(obj, 'TransitNumber', None)
            self.AccountNumber = getattr(obj, 'AccountNumber', None)
            self.AccountOwner = getattr(obj, 'AccountOwner', None)
            self.BankNumber = getattr(obj, 'BankNumber', None)


