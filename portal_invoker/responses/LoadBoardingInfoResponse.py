

from .BaseApiResponse import BaseApiResponse
from ..enums import BoardingStep
from ..enums import CompanyType


class LoadBoardingInfoResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Step = None
            self.CompanyName = None
            self.CompanyAddress = None
            self.AdminFirstName = None
            self.AdminLastName = None
            self.AdminAddress = None
            self.CompanyType = None
            self.DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService = None
            self.DidOwnersAlreadyAskedForBankrupcy = None
            self.HaveYouBeenSubjectOfVisaRiskProgram = None
            self.DrivingLicenceNumber = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Step = BoardingStep(getattr(obj, 'Step', None)) if getattr(obj, 'Step', None) is not None else None
                self.CompanyName = getattr(obj, 'CompanyName', None)
                self.CompanyAddress = getattr(obj, 'CompanyAddress', None)
                self.AdminFirstName = getattr(obj, 'AdminFirstName', None)
                self.AdminLastName = getattr(obj, 'AdminLastName', None)
                self.AdminAddress = getattr(obj, 'AdminAddress', None)
                self.CompanyType = CompanyType(getattr(obj, 'CompanyType', None)) if getattr(obj, 'CompanyType', None) is not None else None
                self.DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService = getattr(obj, 'DidOwnersAlreadyBeenSubjectOfResiliationOfPaymentService', None)
                self.DidOwnersAlreadyAskedForBankrupcy = getattr(obj, 'DidOwnersAlreadyAskedForBankrupcy', None)
                self.HaveYouBeenSubjectOfVisaRiskProgram = getattr(obj, 'HaveYouBeenSubjectOfVisaRiskProgram', None)
                self.DrivingLicenceNumber = getattr(obj, 'DrivingLicenceNumber', None)


