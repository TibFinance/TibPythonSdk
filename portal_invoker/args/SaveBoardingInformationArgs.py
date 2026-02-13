


from ..objects import BoardingInformation


class SaveBoardingInformationArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.IsDraft = None
            self.BoardingInformation = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.IsDraft = getattr(obj, 'IsDraft', None)
            self.BoardingInformation = BoardingInformation(getattr(obj, 'BoardingInformation', None)) if getattr(obj, 'BoardingInformation', None) is not None else None


