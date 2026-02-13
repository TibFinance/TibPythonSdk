


from ..enums import DasFieldType
from ..enums import DasKeyValuePropertyType


class DasKeyValuePropertyBase:
    def __init__(self, obj=None):
        if obj is None:
            
            self.FieldId = None
            self.InnerValue = None
            self.DasKeyValuePropertyType = None

        else:
            
            self.FieldId = DasFieldType(getattr(obj, 'FieldId', None)) if getattr(obj, 'FieldId', None) is not None else None
            self.InnerValue = getattr(obj, 'InnerValue', None)
            self.DasKeyValuePropertyType = DasKeyValuePropertyType(getattr(obj, 'DasKeyValuePropertyType', None)) if getattr(obj, 'DasKeyValuePropertyType', None) is not None else None


