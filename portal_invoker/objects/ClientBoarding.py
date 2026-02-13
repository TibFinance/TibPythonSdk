




class ClientBoarding:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ClientId = None
            self.ClientName = None
            self.ClientEmail = None
            self.ClientPhone = None

        else:
            
            self.ClientId = getattr(obj, 'ClientId', None)
            self.ClientName = getattr(obj, 'ClientName', None)
            self.ClientEmail = getattr(obj, 'ClientEmail', None)
            self.ClientPhone = getattr(obj, 'ClientPhone', None)


