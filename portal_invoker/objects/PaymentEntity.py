
from ..utility import to_enum

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
            
            self.PaymentFlow = to_enum(PaymentFlow, getattr(obj, 'PaymentFlow', None))
            self.Language = to_enum(Language, getattr(obj, 'Language', None))
            self.RelatedCustomerId = getattr(obj, 'RelatedCustomerId', None)
            self.DueDate = getattr(obj, 'DueDate', None)
            self.TransferFrequency = to_enum(TransferFrequency, getattr(obj, 'TransferFrequency', None))
            self.PaymentAmount = getattr(obj, 'PaymentAmount', None)
            self.ForcedCustomerPaymentMethodId = getattr(obj, 'ForcedCustomerPaymentMethodId', None)
            self.GroupId = getattr(obj, 'GroupId', None)
            self.ExternalReferenceIdentification = getattr(obj, 'ExternalReferenceIdentification', None)
            self.AutorizedPaymentMethod = to_enum(AutorizedPaymentMethodFlags, getattr(obj, 'AutorizedPaymentMethod', None))
            self.AskForCustomerConsent = getattr(obj, 'AskForCustomerConsent', None)
            self.IsDeleted = getattr(obj, 'IsDeleted', None)


