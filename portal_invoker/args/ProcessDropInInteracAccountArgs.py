


from ..objects import Interac


class ProcessDropInInteracAccountArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.IsPPAAuthorized = None
            self.InteracInformation = None

        else:
            
            self.IsPPAAuthorized = getattr(obj, 'IsPPAAuthorized', None)
            self.InteracInformation = Interac(getattr(obj, 'InteracInformation', None)) if getattr(obj, 'InteracInformation', None) is not None else None


