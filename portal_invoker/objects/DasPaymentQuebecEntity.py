




class DasPaymentQuebecEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PeriodStartDate = None
            self.PeriodEndDate = None
            self.WithhodingTax = None
            self.RetirementPensionPlan = None
            self.HealthServiceFund = None
            self.ParentalInsurancePlan = None
            self.CNESST = None

        else:
            
            from .DasDateField import DasDateField
            from .DasDateField import DasDateField
            self.PeriodStartDate = DasDateField(getattr(obj, 'PeriodStartDate', None)) if getattr(obj, 'PeriodStartDate', None) is not None else None
            self.PeriodEndDate = DasDateField(getattr(obj, 'PeriodEndDate', None)) if getattr(obj, 'PeriodEndDate', None) is not None else None
            self.WithhodingTax = getattr(obj, 'WithhodingTax', None)
            self.RetirementPensionPlan = getattr(obj, 'RetirementPensionPlan', None)
            self.HealthServiceFund = getattr(obj, 'HealthServiceFund', None)
            self.ParentalInsurancePlan = getattr(obj, 'ParentalInsurancePlan', None)
            self.CNESST = getattr(obj, 'CNESST', None)


