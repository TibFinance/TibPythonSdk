


from ..enums import TibAuthorizationStatus


class EditAuthorizationStatusBulkArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.PaymentIds = None
            self.AuthorizationStatus = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)

            self.PaymentIds = []
            if hasattr(obj, 'PaymentIds') and obj.PaymentIds is not None:
                self.PaymentIds = [name for name in obj.PaymentIds]
            self.AuthorizationStatus = TibAuthorizationStatus(getattr(obj, 'AuthorizationStatus', None)) if getattr(obj, 'AuthorizationStatus', None) is not None else None


