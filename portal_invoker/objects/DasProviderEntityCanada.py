

from .DasProviderBase import DasProviderBase
from ..enums import DasProviderType
from ..enums import DasProviderCanadaFileType
from ..enums import DasProviderCanadaDeclarationFrequency


class DasProviderEntityCanada(DasProviderBase):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.DasProviderType = None
            self.BusinessName = None
            self.BusinessOrAccountNumber = None
            self.FileType = None
            self.FileNumber = None
            self.DeclarationFrequency = None
            self.Description = None

        else:
            super().__init__(obj)

            self.DasProviderType = DasProviderType(getattr(obj, 'DasProviderType', None)) if getattr(obj, 'DasProviderType', None) is not None else None
            self.BusinessName = getattr(obj, 'BusinessName', None)
            self.BusinessOrAccountNumber = getattr(obj, 'BusinessOrAccountNumber', None)
            self.FileType = DasProviderCanadaFileType(getattr(obj, 'FileType', None)) if getattr(obj, 'FileType', None) is not None else None
            self.FileNumber = getattr(obj, 'FileNumber', None)
            self.DeclarationFrequency = DasProviderCanadaDeclarationFrequency(getattr(obj, 'DeclarationFrequency', None)) if getattr(obj, 'DeclarationFrequency', None) is not None else None
            self.Description = getattr(obj, 'Description', None)


