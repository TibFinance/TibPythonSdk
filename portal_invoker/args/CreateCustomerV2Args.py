


from ..objects import CustomerV2


class CreateCustomerV2Args:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.IdempotencyKey = None
            self.ServiceId = None
            self.Customer = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.IdempotencyKey = getattr(obj, 'IdempotencyKey', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.Customer = CustomerV2(getattr(obj, 'Customer', None)) if getattr(obj, 'Customer', None) is not None else None


