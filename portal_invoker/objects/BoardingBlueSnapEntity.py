

from .BoardingEntity import BoardingEntity


class BoardingBlueSnapEntity(BoardingEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BusinessInfo = None
            self.BankingInfo = None
            self.OwnershipInfoArr = None
            self.CompanyRep = None
            self.AdditionalCompanyReps = None
            self.MerchantAgreementsSign = None

        else:
            super().__init__(obj)

            self.BusinessInfo = getattr(obj, 'BusinessInfo', None)
            self.BankingInfo = getattr(obj, 'BankingInfo', None)

            self.OwnershipInfoArr = []
            if hasattr(obj, 'OwnershipInfoArr') and obj.OwnershipInfoArr is not None:
                self.OwnershipInfoArr = [name for name in obj.OwnershipInfoArr]
            self.CompanyRep = getattr(obj, 'CompanyRep', None)

            self.AdditionalCompanyReps = []
            if hasattr(obj, 'AdditionalCompanyReps') and obj.AdditionalCompanyReps is not None:
                self.AdditionalCompanyReps = [name for name in obj.AdditionalCompanyReps]
            self.MerchantAgreementsSign = getattr(obj, 'MerchantAgreementsSign', None)


