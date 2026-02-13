


from ..enums import BoardingIdFileSides
from ..enums import BoardingDocType


class BoardingInformationFileEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Base64 = None
            self.Side = None
            self.IsAdministrator = None
            self.DocType = None

        else:
            
            self.Base64 = getattr(obj, 'Base64', None)
            self.Side = BoardingIdFileSides(getattr(obj, 'Side', None)) if getattr(obj, 'Side', None) is not None else None
            self.IsAdministrator = getattr(obj, 'IsAdministrator', None)
            self.DocType = BoardingDocType(getattr(obj, 'DocType', None)) if getattr(obj, 'DocType', None) is not None else None


