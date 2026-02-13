

from .BaseApiResponse import BaseApiResponse


class GetReferenceInformationResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ReferenceDataString1 = None
            self.ReferenceDataGuid1 = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.ReferenceDataString1 = getattr(obj, 'ReferenceDataString1', None)
                self.ReferenceDataGuid1 = getattr(obj, 'ReferenceDataGuid1', None)


