


from ..enums import Currency
from ..enums import TransferDirection
from ..enums import OperationKind
from ..enums import ProcessStatus


class PaymentOperationWithHierarchy:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PaymentId = None
            self.BillId = None
            self.MerchantId = None
            self.PaymentGroupId = None
            self.OperationAmount = None
            self.Currency = None
            self.OperationDirection = None
            self.OperationKind = None
            self.OperationCreatedDate = None
            self.RelatedPaymentAmount = None
            self.RelatedPaymentConvenientFeesForCreditCard = None
            self.RelatedPaymentConvenientFeesForDirectAccount = None
            self.RelatedPaymentCurrentStatus = None
            self.RelatedPaymentCreatedDate = None
            self.RelatedPaymentCustomerId = None

        else:
            
            self.PaymentId = getattr(obj, 'PaymentId', None)
            self.BillId = getattr(obj, 'BillId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.PaymentGroupId = getattr(obj, 'PaymentGroupId', None)
            self.OperationAmount = getattr(obj, 'OperationAmount', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.OperationDirection = TransferDirection(getattr(obj, 'OperationDirection', None)) if getattr(obj, 'OperationDirection', None) is not None else None
            self.OperationKind = OperationKind(getattr(obj, 'OperationKind', None)) if getattr(obj, 'OperationKind', None) is not None else None
            self.OperationCreatedDate = getattr(obj, 'OperationCreatedDate', None)
            self.RelatedPaymentAmount = getattr(obj, 'RelatedPaymentAmount', None)
            self.RelatedPaymentConvenientFeesForCreditCard = getattr(obj, 'RelatedPaymentConvenientFeesForCreditCard', None)
            self.RelatedPaymentConvenientFeesForDirectAccount = getattr(obj, 'RelatedPaymentConvenientFeesForDirectAccount', None)
            self.RelatedPaymentCurrentStatus = ProcessStatus(getattr(obj, 'RelatedPaymentCurrentStatus', None)) if getattr(obj, 'RelatedPaymentCurrentStatus', None) is not None else None
            self.RelatedPaymentCreatedDate = getattr(obj, 'RelatedPaymentCreatedDate', None)
            self.RelatedPaymentCustomerId = getattr(obj, 'RelatedPaymentCustomerId', None)


