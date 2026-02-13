




class ClientEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ClientName = None

        else:
            
            self.ClientName = getattr(obj, 'ClientName', None)


