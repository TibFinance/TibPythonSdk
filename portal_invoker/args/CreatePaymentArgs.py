


from ..objects import PaymentEntity
from ..enums import AutorizedPaymentMethodFlags


class CreatePaymentArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.BillId = None
            self.SetPaymentCustomerFromBill = None
            self.CustomerEmail = None
            self.PaymentInfo = None
            self.MerchantId = None
            self.ExternalReferenceId = None
            self.SafetyToBreakIfOverRemainingBillAmount = None
            self.AutorizedPaymentMethod = None
            self.AskForCustomerConsent = None
            self.DoNotSendEmail = None
            self.ImmediateTransfer = None
            self.StatementDescription = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.BillId = getattr(obj, 'BillId', None)
            self.SetPaymentCustomerFromBill = getattr(obj, 'SetPaymentCustomerFromBill', None)
            self.CustomerEmail = getattr(obj, 'CustomerEmail', None)
            self.PaymentInfo = PaymentEntity(getattr(obj, 'PaymentInfo', None)) if getattr(obj, 'PaymentInfo', None) is not None else None
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.ExternalReferenceId = getattr(obj, 'ExternalReferenceId', None)
            self.SafetyToBreakIfOverRemainingBillAmount = getattr(obj, 'SafetyToBreakIfOverRemainingBillAmount', None)
            self.AutorizedPaymentMethod = AutorizedPaymentMethodFlags(getattr(obj, 'AutorizedPaymentMethod', None)) if getattr(obj, 'AutorizedPaymentMethod', None) is not None else None
            self.AskForCustomerConsent = getattr(obj, 'AskForCustomerConsent', None)
            self.DoNotSendEmail = getattr(obj, 'DoNotSendEmail', None)
            self.ImmediateTransfer = getattr(obj, 'ImmediateTransfer', None)
            self.StatementDescription = getattr(obj, 'StatementDescription', None)


