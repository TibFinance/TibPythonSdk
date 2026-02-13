




class ClientWithRequestCount:
    def __init__(self, obj=None):
        if obj is None:
            
            self.WaitingRequestsCount = None

        else:
            
            self.WaitingRequestsCount = getattr(obj, 'WaitingRequestsCount', None)


