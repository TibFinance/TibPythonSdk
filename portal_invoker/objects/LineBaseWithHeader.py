

from .LineBase import LineBase


class LineBaseWithHeader(LineBase):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Header = None
            self.StartPosition = None

        else:
            super().__init__(obj)

            from .BaseLineHeader import BaseLineHeader
            self.Header = BaseLineHeader(getattr(obj, 'Header', None)) if getattr(obj, 'Header', None) is not None else None
            self.StartPosition = getattr(obj, 'StartPosition', None)


