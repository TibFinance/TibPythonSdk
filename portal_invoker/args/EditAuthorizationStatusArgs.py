


from ..enums import TibAuthorizationStatus


class EditAuthorizationStatusArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.PaymentId = None
            self.AuthorizationStatus = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.PaymentId = getattr(obj, 'PaymentId', None)
            self.AuthorizationStatus = TibAuthorizationStatus(getattr(obj, 'AuthorizationStatus', None)) if getattr(obj, 'AuthorizationStatus', None) is not None else None


