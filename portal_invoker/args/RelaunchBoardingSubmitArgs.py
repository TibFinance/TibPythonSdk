




class RelaunchBoardingSubmitArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.BoardingInfoId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.BoardingInfoId = getattr(obj, 'BoardingInfoId', None)


