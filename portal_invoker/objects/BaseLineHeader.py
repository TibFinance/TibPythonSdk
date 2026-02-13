

from .LineBase import LineBase
from ..enums import LineType


class BaseLineHeader(LineBase):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.LineType = None
            self.FileNumber = None
            self.OrganizationNumber = None

        else:
            super().__init__(obj)

            self.LineType = LineType(getattr(obj, 'LineType', None)) if getattr(obj, 'LineType', None) is not None else None
            self.FileNumber = getattr(obj, 'FileNumber', None)
            self.OrganizationNumber = getattr(obj, 'OrganizationNumber', None)


