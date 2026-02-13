


from ..enums import PublicAccessTokenRoutingType


class CreateDirectAccountPaymentMethodAndSetToTransferArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AskForCustomerConsent = None
            self.RoutingType = None

        else:
            
            self.AskForCustomerConsent = getattr(obj, 'AskForCustomerConsent', None)
            self.RoutingType = PublicAccessTokenRoutingType(getattr(obj, 'RoutingType', None)) if getattr(obj, 'RoutingType', None) is not None else None


