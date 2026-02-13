

from .BaseApiResponse import BaseApiResponse
from ..objects import ConsolidationInternalReportEntity


class GetConsolidationInternalReportResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ConsolidationInternalReportList = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.ConsolidationInternalReportList = []
                if hasattr(obj, 'ConsolidationInternalReportList') and obj.ConsolidationInternalReportList is not None:
                    self.ConsolidationInternalReportList = [ConsolidationInternalReportEntity(name) for name in  obj.ConsolidationInternalReportList]


