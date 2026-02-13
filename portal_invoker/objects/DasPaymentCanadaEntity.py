




class DasPaymentCanadaEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PeriodEndDate = None
            self.LastPayPeriodEmployeeCount = None
            self.PeriodRawRemuneration = None
            self.PaymentAmount = None

        else:
            
            from .DasMonthlyPeriod import DasMonthlyPeriod
            self.PeriodEndDate = DasMonthlyPeriod(getattr(obj, 'PeriodEndDate', None)) if getattr(obj, 'PeriodEndDate', None) is not None else None
            self.LastPayPeriodEmployeeCount = getattr(obj, 'LastPayPeriodEmployeeCount', None)
            self.PeriodRawRemuneration = getattr(obj, 'PeriodRawRemuneration', None)
            self.PaymentAmount = getattr(obj, 'PaymentAmount', None)


