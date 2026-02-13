


from ..objects import CustomerEntity


class CreateCustomerArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ServiceId = None
            self.Customer = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.Customer = CustomerEntity(getattr(obj, 'Customer', None)) if getattr(obj, 'Customer', None) is not None else None


