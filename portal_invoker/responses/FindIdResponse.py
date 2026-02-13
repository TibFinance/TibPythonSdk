

from .BaseApiResponse import BaseApiResponse


class FindIdResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.RelatedClientId = None
            self.ClientName = None
            self.TableName = None
            self.RelatedDescription = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.RelatedClientId = getattr(obj, 'RelatedClientId', None)
                self.ClientName = getattr(obj, 'ClientName', None)
                self.TableName = getattr(obj, 'TableName', None)
                self.RelatedDescription = getattr(obj, 'RelatedDescription', None)


