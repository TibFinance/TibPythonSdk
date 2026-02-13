




class GetServiceBoardingStatusArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.BoardingServiceId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.BoardingServiceId = getattr(obj, 'BoardingServiceId', None)


