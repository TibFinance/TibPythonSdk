


from ..enums import PublicAccessTokenRoutingType
from ..objects import CreditCard


class CreateCreditCardPaymentMethodAndSetToTransferArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.IsCustomerAutomaticPaymentMethod = None
            self.CreditCard = None
            self.AskForCustomerConsent = None
            self.RoutingType = None

        else:
            
            self.IsCustomerAutomaticPaymentMethod = getattr(obj, 'IsCustomerAutomaticPaymentMethod', None)
            self.CreditCard = CreditCard(getattr(obj, 'CreditCard', None)) if getattr(obj, 'CreditCard', None) is not None else None
            self.AskForCustomerConsent = getattr(obj, 'AskForCustomerConsent', None)
            self.RoutingType = PublicAccessTokenRoutingType(getattr(obj, 'RoutingType', None)) if getattr(obj, 'RoutingType', None) is not None else None


