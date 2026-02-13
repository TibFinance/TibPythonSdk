




class UpdateBoardingStatusArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.BoardingInformationId = None
            self.BoardingStatus = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.BoardingInformationId = getattr(obj, 'BoardingInformationId', None)
            self.BoardingStatus = getattr(obj, 'BoardingStatus', None)


