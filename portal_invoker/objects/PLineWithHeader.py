

from .LineBaseWithHeader import LineBaseWithHeader


class PLineWithHeader(LineBaseWithHeader):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            pass
        else:
            super().__init__(obj)

            pass

