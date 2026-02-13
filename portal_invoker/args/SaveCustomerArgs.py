


from ..objects import Customer


class SaveCustomerArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.Customer = None
            self.MerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.Customer = Customer(getattr(obj, 'Customer', None)) if getattr(obj, 'Customer', None) is not None else None
            self.MerchantId = getattr(obj, 'MerchantId', None)


