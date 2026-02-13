


from ..enums import PaymentFlow
from ..enums import Language
from ..enums import TransferFrequency
from ..enums import AutorizedPaymentMethodFlags


class PaymentEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PaymentFlow = None
            self.Language = None
            self.RelatedCustomerId = None
            self.DueDate = None
            self.TransferFrequency = None
            self.PaymentAmount = None
            self.ForcedCustomerPaymentMethodId = None
            self.GroupId = None
            self.ExternalReferenceIdentification = None
            self.AutorizedPaymentMethod = None
            self.AskForCustomerConsent = None
            self.IsDeleted = None

        else:
            
            self.PaymentFlow = PaymentFlow(getattr(obj, 'PaymentFlow', None)) if getattr(obj, 'PaymentFlow', None) is not None else None
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.RelatedCustomerId = getattr(obj, 'RelatedCustomerId', None)
            self.DueDate = getattr(obj, 'DueDate', None)
            self.TransferFrequency = TransferFrequency(getattr(obj, 'TransferFrequency', None)) if getattr(obj, 'TransferFrequency', None) is not None else None
            self.PaymentAmount = getattr(obj, 'PaymentAmount', None)
            self.ForcedCustomerPaymentMethodId = getattr(obj, 'ForcedCustomerPaymentMethodId', None)
            self.GroupId = getattr(obj, 'GroupId', None)
            self.ExternalReferenceIdentification = getattr(obj, 'ExternalReferenceIdentification', None)
            self.AutorizedPaymentMethod = AutorizedPaymentMethodFlags(getattr(obj, 'AutorizedPaymentMethod', None)) if getattr(obj, 'AutorizedPaymentMethod', None) is not None else None
            self.AskForCustomerConsent = getattr(obj, 'AskForCustomerConsent', None)
            self.IsDeleted = getattr(obj, 'IsDeleted', None)


