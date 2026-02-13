

from .DasKeyValuePropertyBase import DasKeyValuePropertyBase
from ..enums import DasKeyValuePropertyType


class DasKeyValueProperty(DasKeyValuePropertyBase):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Value = None
            self.InnerValue = None
            self.DasKeyValuePropertyType = None

        else:
            super().__init__(obj)

            self.Value = getattr(obj, 'Value', None)
            self.InnerValue = getattr(obj, 'InnerValue', None)
            self.DasKeyValuePropertyType = DasKeyValuePropertyType(getattr(obj, 'DasKeyValuePropertyType', None)) if getattr(obj, 'DasKeyValuePropertyType', None) is not None else None


