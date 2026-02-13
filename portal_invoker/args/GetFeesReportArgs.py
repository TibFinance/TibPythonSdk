


from ..enums import PaymentMethodType
from ..enums import OperationKind


class GetFeesReportArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.ServiceId = None
            self.DateFrom = None
            self.DateTo = None
            self.PaymentMethodType = None
            self.FeeType = None
            self.IncludeDetails = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.DateFrom = getattr(obj, 'DateFrom', None)
            self.DateTo = getattr(obj, 'DateTo', None)
            self.PaymentMethodType = PaymentMethodType(getattr(obj, 'PaymentMethodType', None)) if getattr(obj, 'PaymentMethodType', None) is not None else None
            self.FeeType = OperationKind(getattr(obj, 'FeeType', None)) if getattr(obj, 'FeeType', None) is not None else None
            self.IncludeDetails = getattr(obj, 'IncludeDetails', None)


