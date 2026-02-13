


from ..enums import BoardingIdFileSides


class BoardingInfoFileEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Base64 = None
            self.Side = None
            self.IsAdministrator = None

        else:
            
            self.Base64 = getattr(obj, 'Base64', None)
            self.Side = BoardingIdFileSides(getattr(obj, 'Side', None)) if getattr(obj, 'Side', None) is not None else None
            self.IsAdministrator = getattr(obj, 'IsAdministrator', None)


