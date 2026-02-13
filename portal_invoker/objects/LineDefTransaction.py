

from .LineBaseWithHeader import LineBaseWithHeader


class LineDefTransaction(LineBaseWithHeader):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Segments = None

        else:
            super().__init__(obj)

            from .BaseTransaction import BaseTransaction

            self.Segments = []
            if hasattr(obj, 'Segments') and obj.Segments is not None:
                self.Segments = [BaseTransaction(name) for name in  obj.Segments]


