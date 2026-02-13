

from .BaseLineHeader import BaseLineHeader
from ..enums import LineType


class LineDefHeader(BaseLineHeader):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.LineType = None
            self.RowNumber = None
            self.OrganizationNumber = None
            self.FileNumber = None

        else:
            super().__init__(obj)

            self.LineType = LineType(getattr(obj, 'LineType', None)) if getattr(obj, 'LineType', None) is not None else None
            self.RowNumber = getattr(obj, 'RowNumber', None)
            self.OrganizationNumber = getattr(obj, 'OrganizationNumber', None)
            self.FileNumber = getattr(obj, 'FileNumber', None)


