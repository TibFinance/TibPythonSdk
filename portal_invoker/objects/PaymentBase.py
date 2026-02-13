


from ..enums import ProcessStatus
from ..enums import PaymentMethodType


class PaymentBase:
    def __init__(self, obj=None):
        if obj is None:
            
            self.BillId = None
            self.BillExternalSystemNumber1 = None
            self.BillExternalSystemNumber2 = None
            self.BillExternalSystemNumber3 = None
            self.BillTitle = None
            self.RelatedCustomerId = None
            self.RelatedCustomerExternalId = None
            self.BillDescription = None
            self.PaymentId = None
            self.IsAutomaticPayment = None
            self.PaymentInfo = None
            self.IsMarkResolved = None
            self.CurrentStatus = None
            self.ConvenientFeeCreditCard = None
            self.ConvenientFeeDirectAccount = None
            self.CreatedDate = None
            self.PaymentMethodDescription = None
            self.AccountInformationPreview = None
            self.PaymentMethodType = None

        else:
            
            from .PaymentEntity import PaymentEntity
            self.BillId = getattr(obj, 'BillId', None)
            self.BillExternalSystemNumber1 = getattr(obj, 'BillExternalSystemNumber1', None)
            self.BillExternalSystemNumber2 = getattr(obj, 'BillExternalSystemNumber2', None)
            self.BillExternalSystemNumber3 = getattr(obj, 'BillExternalSystemNumber3', None)
            self.BillTitle = getattr(obj, 'BillTitle', None)
            self.RelatedCustomerId = getattr(obj, 'RelatedCustomerId', None)
            self.RelatedCustomerExternalId = getattr(obj, 'RelatedCustomerExternalId', None)
            self.BillDescription = getattr(obj, 'BillDescription', None)
            self.PaymentId = getattr(obj, 'PaymentId', None)
            self.IsAutomaticPayment = getattr(obj, 'IsAutomaticPayment', None)
            self.PaymentInfo = PaymentEntity(getattr(obj, 'PaymentInfo', None)) if getattr(obj, 'PaymentInfo', None) is not None else None
            self.IsMarkResolved = getattr(obj, 'IsMarkResolved', None)
            self.CurrentStatus = ProcessStatus(getattr(obj, 'CurrentStatus', None)) if getattr(obj, 'CurrentStatus', None) is not None else None
            self.ConvenientFeeCreditCard = getattr(obj, 'ConvenientFeeCreditCard', None)
            self.ConvenientFeeDirectAccount = getattr(obj, 'ConvenientFeeDirectAccount', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.PaymentMethodDescription = getattr(obj, 'PaymentMethodDescription', None)
            self.AccountInformationPreview = getattr(obj, 'AccountInformationPreview', None)
            self.PaymentMethodType = PaymentMethodType(getattr(obj, 'PaymentMethodType', None)) if getattr(obj, 'PaymentMethodType', None) is not None else None


